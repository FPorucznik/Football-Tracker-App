from urllib.request import urlopen
import json

#pobieram dane z API uwzględniając wybraną lige po kodzie z argumentu i następnie zwracam każdą drużynę, jej miejsce w tabeli, zagrane mecze, wygrane, remisy, przegrane
def table(leagueCode):
    api_key = "744cd392b976057dc9f075224d2fecac0fda9d7a73645b21792f386eec691b51"
    api_url = "https://apiv2.apifootball.com/?action=get_standings&league_id="+leagueCode+"&APIkey="+api_key

    result = urlopen(api_url)

    data = json.load(result)
    listed_data = []

    for item in data:
        listed_data.append([item['overall_league_position'],item['team_name'],item['overall_league_payed'],item['overall_league_W'],item['overall_league_D'],item['overall_league_L']])

    return listed_data
