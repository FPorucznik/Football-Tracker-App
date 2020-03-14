import tkinter as tk
from tkinter.font import Font
#Football Tracker alpha version

#wygenerowanie okna
window = tk.Tk()
window.geometry("500x500+400+100")
window.title("Football Tracker")
window.iconbitmap("assets/football.ico")

#powitalny tekst
welcome = tk.Label(text = "Witaj w aplikacji Football Tracker", font="Arial")
welcome.pack(pady=30)

buttonTables = tk.Button(text = "Tabele", width = 20, height = 2, font="Arial")
buttonTables.pack(pady=20)
buttonGoalScorers = tk.Button(text = "Klasyfikacja strzelców", width = 20, height = 2, font="Arial")
buttonGoalScorers.pack(pady=20)
buttonMatches = tk.Button(text = "Dzisiejsze mecze", width = 20, height = 2, font="Arial")
buttonMatches.pack(pady=20)

window.mainloop()