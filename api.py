from urllib.request import urlopen
import json
import operator
from datetime import date
import http.client

#pobieram dane z API uwzględniając wybraną lige po kodzie z argumentu i następnie zwracam każdą drużynę, jej miejsce w tabeli, zagrane mecze, wygrane, remisy, przegrane i punkty
api_key = "744cd392b976057dc9f075224d2fecac0fda9d7a73645b21792f386eec691b51"
matches_key = "17ea1222bc094dcf930c6d1385ed87c2" #dołączam do projektu drugie api ponieważ w pierwszym nie ma aktualnych meczów dla każdego dnia
def table(leagueCode):
    api_url = "https://apiv2.apifootball.com/?action=get_standings&league_id="+leagueCode+"&APIkey="+api_key

    result = urlopen(api_url)

    data = json.load(result)
    listed_data = []

    for item in data:
        listed_data.append([item['overall_league_position'],item['team_name'],item['overall_league_payed'],item['overall_league_W'],item['overall_league_D'],item['overall_league_L'],item['overall_league_PTS']])

    return listed_data

def scorers(leagueCode):
    api_url = "https://apiv2.apifootball.com/?action=get_teams&league_id="+leagueCode+"&APIkey="+api_key
    result = urlopen(api_url)

    data = json.load(result)
    
    teams_data_lists = []
    players_list = []
    '''
    tutaj sytuacja się skomplikowała ponieważ api, z którego korzystam
    nie zawiera bezpośrednio zapytania dotyczącego strzelców, ale znalazłem
    sposób by to obejść i korzystam ze spisu wszystkich zawodników z drużyn z danej ligi, w których gole każdego zawodnika są do niego przypisane
    '''
    for i in range(0,len(data)):
        teams_data_lists.append(data[i]['players'])
    
    for i in range(0,len(teams_data_lists)):
        for j in range(0,len(teams_data_lists[i])):
            players_list.append(teams_data_lists[i][j])

    '''
    wszystko po przekształceniu zamieniam na słownik w formacie
    'zawodnik' : strzelone bramki
    '''

    players = []
    goals = []

    for i in range(0,len(players_list)):
        players.append(players_list[i]['player_name'])
        goals.append(players_list[i]['player_goals'])
    
    goals = [int(x) for x in goals]
    
    final_statistics = dict(zip(players,goals))

    sorted_goalScorers = dict(sorted(final_statistics.items(), key=operator.itemgetter(1),reverse=True))#posortowanie słownika malejąco według goli, dzięki temu lista najlepszych strzelców widnieje już w słowniku
    
    return sorted_goalScorers

def matches_today(leagueCode):
    today = str(date.today())

    #kody lig z drugiego api
    #bundes BL1
    #prem   PL
    #laliga PD
    #serie SA
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': matches_key }
    connection.request('GET', '/v2/competitions/'+leagueCode+'/matches?dateFrom='+today+'&dateTo='+today+'', None, headers )
    response = json.loads(connection.getresponse().read().decode())#drugie api wymaga takiego polaczenia

    dates = []
    matchUps = []
    for i in range(0,len(response['matches'])):
        current = response['matches'][i]['utcDate']#formatowanie zwracanej daty z api
        current_formatted = current.replace('Z','')
        current_formatted = current_formatted.replace('T',' ')
        current_formatted = current_formatted[11:16]
        hour = int(current_formatted[0:2])

        if hour != 0:
            hour = str(hour + 2)#dodanie godzin ze względu na inną strefę czasową
            current_formatted = current_formatted.replace(current_formatted[0:2],hour)
        else:
            current_formatted = current_formatted.replace("0"+current_formatted[0:2],str(hour))
        dates.append(current_formatted)

        matchUps.append(response['matches'][i]['homeTeam']['name'] + '  :  ' + response['matches'][i]['awayTeam']['name'])

    full_matches_data = dict(zip(matchUps,dates))
    return full_matches_data



    


