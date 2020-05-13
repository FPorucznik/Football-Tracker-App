#Football Tracker alpha version
import tkinter as tk #biblioteka do GUI
from tkinter import *
from tkinter import ttk
import api #moduł z zapytaniami api
from datetime import date
from time import strftime
from PIL import Image, ImageTk

#wygenerowanie okna
window = tk.Tk()
window.geometry("600x600+400+20")
window.title("Football Tracker")
window.iconbitmap("assets/football.ico")
window.resizable(0,0)

#funkcja czyszcząca okno, wykorzystuje ją przy wyborze opcji z menu
def clearWindow():
    children = window.winfo_children()
    for child in children:
        child.destroy()

#menu startowe
def welcomeMenu():
    clearWindow()
    
    canvas = tk.Canvas(window, width=600, height=600)
    canvas.pack()
    background = ImageTk.PhotoImage(Image.open("assets/background.png"))
    canvas.background = background
    canvas.create_image(0, 0, image=background, anchor=NW)

    welcome_window = canvas.create_text(300, 50, anchor=N, font=("Russo One", 20), fill="white", text="Witaj w aplikacji Football Tracker")

    buttonTables = tk.Button(text = "Tabele", width=20, font=("Russo One", 15), command=tables)
    buttonTables_window = canvas.create_window(300,120, anchor=N, window=buttonTables)

    buttonGoalScorers = tk.Button(text = "Klasyfikacja strzelców", width = 20, font=("Russo One", 15), command=goalScorers)
    buttonGoalScorers_window = canvas.create_window(300,220, anchor=N, window=buttonGoalScorers)

    buttonMatches = tk.Button(text = "Dzisiejsze mecze", width = 20, font=("Russo One", 15), command=matches)
    buttonMatches_window = canvas.create_window(300,320, anchor=N, window=buttonMatches)

#sekcja tabel
def tables():
    clearWindow()

    canvas = tk.Canvas(window, width=600, height=600)
    canvas.pack()
    background = ImageTk.PhotoImage(Image.open("assets/bgleagues.png"))
    canvas.background = background
    canvas.create_image(0, 0, image=background, anchor=NW)

    info_text = canvas.create_text(300, 50, anchor=N, font=("Russo One", 20), fill="black", text="Wybierz Ligę")

    buttonReturn = tk.Button(text = "<- Wróć do menu", width = 20, font=("Russo One", 10), command=welcomeMenu)
    buttonReturn_window = canvas.create_window(80,15, anchor=N, window=buttonReturn)

    buttonPremierLeague = tk.Button(text = "Premier League", width = 20, font=("Russo One", 15), command = lambda: leagueTable("148","Premier League"))#tutaj w każdym przycisku w command jako argument przekazuje kod ligi, który sprawdziłem w dokumentacji API oraz nazwe ligi dla odpowiedniego podpisy
    buttonPremierLeague = canvas.create_window(300,130, anchor=N, window=buttonPremierLeague)

    buttonLaLiga = tk.Button(text = "LaLiga", width = 20, font=("Russo One", 15), command = lambda: leagueTable("468","LaLiga"))
    buttonPremierLeague = canvas.create_window(300,210, anchor=N, window=buttonLaLiga)

    buttonBundesliga = tk.Button(text = "Bundesliga", width = 20, font=("Russo One", 15), command = lambda: leagueTable("195","Bundesliga"))
    buttonBundesliga = canvas.create_window(300,280, anchor=N, window=buttonBundesliga)

    buttonSerieA = tk.Button(text = "Serie A", width = 20, font=("Russo One", 15), command = lambda: leagueTable("262","Serie A"))
    buttonSerieA = canvas.create_window(300,355, anchor=N, window=buttonSerieA)

#sekcja strzelców
def goalScorers():
    clearWindow()

    canvas = tk.Canvas(window, width=600, height=600)
    canvas.pack()
    background = ImageTk.PhotoImage(Image.open("assets/bgleagues.png"))
    canvas.background = background
    canvas.create_image(0, 0, image=background, anchor=NW)

    info_text = canvas.create_text(300, 50, anchor=N, font=("Russo One", 20), fill="black", text="Klasyfikacja strzelców")

    buttonReturn = tk.Button(text = "<- Wróć do menu", width = 20, font=("Russo One", 10), command=welcomeMenu)
    buttonReturn_window = canvas.create_window(80,15, anchor=N, window=buttonReturn)

    buttonPremierLeague = tk.Button(text = "Premier League", width = 20, font=("Russo One", 15), command = lambda: scorerTable("148","Premier League"))#tutaj w każdym przycisku w command jako argument przekazuje kod ligi, który sprawdziłem w dokumentacji API oraz nazwe ligi dla odpowiedniego podpisy
    buttonPremierLeague = canvas.create_window(300,130, anchor=N, window=buttonPremierLeague)

    buttonLaLiga = tk.Button(text = "LaLiga", width = 20, font=("Russo One", 15), command = lambda: scorerTable("468","LaLiga"))
    buttonPremierLeague = canvas.create_window(300,210, anchor=N, window=buttonLaLiga)

    buttonBundesliga = tk.Button(text = "Bundesliga", width = 20, font=("Russo One", 15), command = lambda: scorerTable("195","Bundesliga"))
    buttonBundesliga = canvas.create_window(300,280, anchor=N, window=buttonBundesliga)

    buttonSerieA = tk.Button(text = "Serie A", width = 20, font=("Russo One", 15), command = lambda: scorerTable("262","Serie A"))
    buttonSerieA = canvas.create_window(300,355, anchor=N, window=buttonSerieA)

#sekcja meczów
def matches():
    clearWindow()

    canvas = tk.Canvas(window, width=600, height=600)
    canvas.pack()
    background = ImageTk.PhotoImage(Image.open("assets/bgleagues.png"))
    canvas.background = background
    canvas.create_image(0, 0, image=background, anchor=NW)

    info_text = canvas.create_text(300, 50, anchor=N, font=("Russo One", 20), fill="black", text="Dzisiejsze mecze")

    buttonReturn = tk.Button(text = "<- Wróć do menu", width = 20, font=("Russo One", 10), command=welcomeMenu)
    buttonReturn_window = canvas.create_window(80,15, anchor=N, window=buttonReturn)

    buttonPremierLeague = tk.Button(text = "Premier League", width = 20, font=("Russo One", 15), command = lambda: matches_schedule("PL","Premier League"))#tutaj w każdym przycisku w command jako argument przekazuje kod ligi, który sprawdziłem w dokumentacji drugiego API oraz nazwe ligi dla odpowiedniego podpisu
    buttonPremierLeague = canvas.create_window(300,130, anchor=N, window=buttonPremierLeague)

    buttonLaLiga = tk.Button(text = "LaLiga", width = 20, font=("Russo One", 15), command = lambda: matches_schedule("PD","LaLiga"))
    buttonPremierLeague = canvas.create_window(300,210, anchor=N, window=buttonLaLiga)

    buttonBundesliga = tk.Button(text = "Bundesliga", width = 20, font=("Russo One", 15), command = lambda: matches_schedule("BL1","Bundesliga"))
    buttonBundesliga = canvas.create_window(300,280, anchor=N, window=buttonBundesliga)

    buttonSerieA = tk.Button(text = "Serie A", width = 20, font=("Russo One", 15), command = lambda: matches_schedule("SA","Serie A"))
    buttonSerieA = canvas.create_window(300,355, anchor=N, window=buttonSerieA)

def leagueTable(league_code,league_name):
    clearWindow()
    
    canvas = tk.Canvas(window, width=600, height=600)
    canvas.pack()
    if league_name == "Premier League":
        background = ImageTk.PhotoImage(Image.open("assets/bgprem.png"))
    elif league_name == "LaLiga":
        background = ImageTk.PhotoImage(Image.open("assets/bglaliga.png"))
    elif league_name == "Bundesliga":
        background = ImageTk.PhotoImage(Image.open("assets/bgbundes.png"))
    else:
        background = ImageTk.PhotoImage(Image.open("assets/bgserie.png"))
    canvas.background = background
    canvas.create_image(0, 0, image=background, anchor=NW)

    buttonReturn = tk.Button(text = "<- Wróć do lig", width = 20, font=("Russo One", 10), command=tables)
    buttonReturn_window = canvas.create_window(80,15, anchor=N, window=buttonReturn)

    info_text = canvas.create_text(300, 50, anchor=N, font=("Russo One", 20), fill="black", text=league_name)

    #funkcja api.table zwraca nam liste danych o danej lidze, znajduje się ona w pliku api.py
    table_data = api.table(league_code)

    #stworzenie tabeli za pomocą narzędzi z tkinter
    tableFrame = Frame(window)
    tableFrame.pack()

    frame_window = canvas.create_window(300, 300, window=tableFrame)

    tableContent = ttk.Treeview(tableFrame, columns=(1,2,3,4,5,6,7), show="headings", height="20")
    tableContent.pack()

    tableContent.heading(1, text="Miejsce")
    tableContent.column(1, minwidth=0, width=50)
    tableContent.heading(2, text="Nazwa")
    tableContent.column(2, minwidth=0, width=150)
    tableContent.heading(3, text="M")
    tableContent.column(3, minwidth=0, width=50)
    tableContent.heading(4, text="W")
    tableContent.column(4, minwidth=0, width=50)
    tableContent.heading(5, text="R")
    tableContent.column(5, minwidth=0, width=50)
    tableContent.heading(6, text="P")
    tableContent.column(6, minwidth=0, width=50)
    tableContent.heading(7, text="Pkt")
    tableContent.column(7, minwidth=0, width=50)

    #wstawienie rekordów do tabeli
    for item in table_data:
        tableContent.insert('', 'end', values=item)

def scorerTable(league_code,league_name):
    clearWindow()

    canvas = tk.Canvas(window, width=600, height=600)
    canvas.pack()
    if league_name == "Premier League":
        background = ImageTk.PhotoImage(Image.open("assets/bgprem.png"))
    elif league_name == "LaLiga":
        background = ImageTk.PhotoImage(Image.open("assets/bglaliga.png"))
    elif league_name == "Bundesliga":
        background = ImageTk.PhotoImage(Image.open("assets/bgbundes.png"))
    else:
        background = ImageTk.PhotoImage(Image.open("assets/bgserie.png"))
    canvas.background = background
    canvas.create_image(0, 0, image=background, anchor=NW)

    buttonReturn = tk.Button(text = "<- Wróć do lig", width = 20, font=("Russo One", 10), command=goalScorers)
    buttonReturn_window = canvas.create_window(80,15, anchor=N, window=buttonReturn)

    info_text = canvas.create_text(300, 50, anchor=N, font=("Russo One", 20), fill="black", text=league_name)

    #funkcja api.scorers zwraca nam słownik strzelców, znajduje się ona w pliku api.py
    scorers_data = api.scorers(league_code)

    tableFrame = Frame(window)
    tableFrame.pack()

    frame_window = canvas.create_window(300, 300, window=tableFrame)

    tableContent = ttk.Treeview(tableFrame, columns=(1,2,3), show="headings", height="20")
    tableContent.pack()

    tableContent.heading(1, text="Miejsce")
    tableContent.column(1, minwidth=0, width=100)
    tableContent.heading(2, text="Zawodnik")
    tableContent.column(2, minwidth=0, width=200)
    tableContent.heading(3, text="Strzelone bramki")
    tableContent.column(3, minwidth=0, width=100)

    #wstawienie rekordów do tabeli
    counter = 0
    for k, v in scorers_data.items():
        counter = counter + 1
        tableContent.insert('', 'end', values=(counter,k,v))

def matches_schedule(league_code,league_name):
    clearWindow()

    canvas = tk.Canvas(window, width=600, height=600)
    canvas.pack()
    if league_name == "Premier League":
        background = ImageTk.PhotoImage(Image.open("assets/bgprem.png"))
    elif league_name == "LaLiga":
        background = ImageTk.PhotoImage(Image.open("assets/bglaliga.png"))
    elif league_name == "Bundesliga":
        background = ImageTk.PhotoImage(Image.open("assets/bgbundes.png"))
    else:
        background = ImageTk.PhotoImage(Image.open("assets/bgserie.png"))
    canvas.background = background
    canvas.create_image(0, 0, image=background, anchor=NW)

    buttonReturn = tk.Button(text = "<- Wróć do lig", width = 20, font=("Russo One", 10), command=matches)
    buttonReturn_window = canvas.create_window(80,15, anchor=N, window=buttonReturn)

    info_text = canvas.create_text(300, 30, anchor=N, font=("Russo One", 20), fill="black", text=league_name)

    today=date.today()
    today=today.strftime("%d.%m.%Y")

    date_text = canvas.create_text(180, 80, anchor=N, font=("Russo One", 20), fill="black", text="Data: "+today)

    time = strftime('%H:%M') 
    time_text = canvas.create_text(420, 80, anchor=N, font=("Russo One", 20), fill="black", text="Godzina: "+time)

    
    matches_data = api.matches_today(league_code)
    if matches_data == {}:
        msg = canvas.create_text(300, 200, anchor=N, font=("Russo One", 20), fill="black", text="Brak meczów w tym dniu")
    else:
        tableFrame = Frame(window)
        tableFrame.pack()

        frame_window = canvas.create_window(300, 330, window=tableFrame)

        tableContent = ttk.Treeview(tableFrame, columns=(1,2), show="headings", height="20")
        tableContent.pack()

        tableContent.heading(1, text="Mecz")
        tableContent.column(1, minwidth=0, width=300)
        tableContent.heading(2, text="Godzina")
        tableContent.column(2, minwidth=0, width=100)

        for k, v in matches_data.items():
            tableContent.insert('', 'end', values=(k,v))



welcomeMenu()
window.mainloop()