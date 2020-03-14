#Football Tracker alpha version
import tkinter as tk

#wygenerowanie okna
window = tk.Tk()
window.geometry("500x500+400+100")
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

    buttonPremierLeague = tk.Button(text = "Premier League", width = 20, height = 1, font="Arial")
    buttonPremierLeague.pack(pady=10)

    buttonLaLiga = tk.Button(text = "LaLiga", width = 20, height = 1, font="Arial")
    buttonLaLiga.pack(pady=10)

    buttonBundesliga = tk.Button(text = "Bundesliga", width = 20, height = 1, font="Arial")
    buttonBundesliga.pack(pady=10)

    buttonSerieA = tk.Button(text = "Serie A", width = 20, height = 1, font="Arial")
    buttonSerieA.pack(pady=10)

#sekcja strzelców
def goalScorers():
    clearWindow()
    title = tk.Label(text = "Klasyfikacja strzelców", font="Arial")
    title.pack()

    buttonReturn = tk.Button(text = "Wróć do menu", width = 20, height = 1, font="Arial", command=welcomeMenu)
    buttonReturn.pack(pady=20)

#sekcja meczów
def matches():
    clearWindow()
    title = tk.Label(text = "Dzisiejsze mecze", font="Arial")
    title.pack()

    buttonReturn = tk.Button(text = "Wróć do menu", width = 20, height = 1, font="Arial", command=welcomeMenu)
    buttonReturn.pack(pady=20)

welcomeMenu()
window.mainloop()