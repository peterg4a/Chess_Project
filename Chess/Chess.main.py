import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title("The 5 Gambit")
root.geometry("800x800")
test = tk.PhotoImage(file = 'Chess/pieces/bbishop.png')
tk.Label(root, image=test).pack()
root.mainloop()

