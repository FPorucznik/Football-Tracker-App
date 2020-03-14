import tkinter as tk
#Football Tracker alpha version

#wygenerowanie okna
window = tk.Tk()
window.geometry("500x500+400+100")
window.title("Football Tracker")
window.iconbitmap("assets/football.ico")

#powitalny tekst
welcome = tk.Label(text = "Witaj w aplikacji Football Tracker")
welcome.pack()

buttonTables = tk.Button(text = "Tabele", width = 20, height = 5)
buttonTables.pack()

window.mainloop()