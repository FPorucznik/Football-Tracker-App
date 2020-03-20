#Football Tracker alpha version
import tkinter as tk #biblioteka do GUI
from tkinter import *
from tkinter import ttk
import api #moduł z zapytaniami api

#wygenerowanie okna
window = tk.Tk()
window.geometry("500x600+400+20")
window.title("Football Tracker")
window.iconbitmap("assets/football.ico")

#funkcja czyszcząca okno, wykorzystuje ją przy wyborze opcji z menu
def clearWindow():
    children = window.winfo_children()
    for child in children:
        child.destroy()

#menu startowe
def welcomeMenu():
    clearWindow()
    welcome = tk.Label(text = "Witaj w aplikacji Football Tracker", font="Arial")
    welcome.pack(pady=30)

    buttonTables = tk.Button(text = "Tabele", width = 20, height = 2, font="Arial", command=tables)
    buttonTables.pack(pady=20)
    buttonGoalScorers = tk.Button(text = "Klasyfikacja strzelców", width = 20, height = 2, font="Arial", command=goalScorers)
    buttonGoalScorers.pack(pady=20)
    buttonMatches = tk.Button(text = "Dzisiejsze mecze", width = 20, height = 2, font="Arial", command=matches)
    buttonMatches.pack(pady=20)

#sekcja tabel
def tables():
    clearWindow()
    title = tk.Label(text = "Wybierz Ligę", font="Arial")
    title.pack()

    buttonReturn = tk.Button(text = "Wróć do menu", width = 20, height = 1, font="Arial", command=welcomeMenu)
    buttonReturn.pack(pady=20)

    buttonPremierLeague = tk.Button(text = "Premier League", width = 20, height = 1, font="Arial", command = lambda: leagueTable("148"))#tutaj w każdym przycisku w command jako argument przekazuje kod ligi, który sprawdziłem w dokumentacji API
    buttonPremierLeague.pack(pady=10)

    buttonLaLiga = tk.Button(text = "LaLiga", width = 20, height = 1, font="Arial", command = lambda: leagueTable("468"))
    buttonLaLiga.pack(pady=10)

    buttonBundesliga = tk.Button(text = "Bundesliga", width = 20, height = 1, font="Arial", command = lambda: leagueTable("195"))
    buttonBundesliga.pack(pady=10)

    buttonSerieA = tk.Button(text = "Serie A", width = 20, height = 1, font="Arial", command = lambda: leagueTable("262"))
    buttonSerieA.pack(pady=10)

#sekcja strzelców
def goalScorers():
    clearWindow()
    title = tk.Label(text = "Klasyfikacja strzelców", font="Arial")
    title.pack()

    buttonReturn = tk.Button(text = "Wróć do menu", width = 20, height = 1, font="Arial", command=welcomeMenu)
    buttonReturn.pack(pady=20)

    buttonPremierLeague = tk.Button(text = "Premier League", width = 20, height = 1, font="Arial", command = lambda: scorerTable("148"))#tutaj w każdym przycisku w command jako argument przekazuje kod ligi, który sprawdziłem w dokumentacji API
    buttonPremierLeague.pack(pady=10)

    buttonLaLiga = tk.Button(text = "LaLiga", width = 20, height = 1, font="Arial", command = lambda: scorerTable("468"))
    buttonLaLiga.pack(pady=10)

    buttonBundesliga = tk.Button(text = "Bundesliga", width = 20, height = 1, font="Arial", command = lambda: scorerTable("195"))
    buttonBundesliga.pack(pady=10)

    buttonSerieA = tk.Button(text = "Serie A", width = 20, height = 1, font="Arial", command = lambda: scorerTable("262"))
    buttonSerieA.pack(pady=10)

#sekcja meczów
def matches():
    clearWindow()
    title = tk.Label(text = "Dzisiejsze mecze", font="Arial")
    title.pack()

    buttonReturn = tk.Button(text = "Wróć do menu", width = 20, height = 1, font="Arial", command=welcomeMenu)
    buttonReturn.pack(pady=20)

def leagueTable(league_code):
    clearWindow()

    buttonReturn = tk.Button(text = "Wróć do lig", width = 20, height = 1, font="Arial", command=tables)
    buttonReturn.pack(pady=20)

    #funkcja api.table zwraca nam liste danych o danej lidze, znajduje się ona w pliku api.py
    table_data = api.table(league_code)

    #stworzenie tabeli za pomocą narzędzi z tkinter
    tableFrame = Frame(window)
    tableFrame.pack()

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

welcomeMenu()
window.mainloop()