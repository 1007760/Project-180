from tkinter import *
from tkinter import ttk
from googletrans import Translator
root = Tk()
root.configure(bg = "teal")
root.geometry("500x500")
root.title("Project 180")

title = Label(root, text = "LANGUAGE TRANSLATOR", bg = "teal", font = ("Sylfaen", 20, "bold"))
title.place(relx = 0.5, rely = 0.1, anchor = CENTER)
display = Label(root, text = "Enter Text", bg = "teal", font = ("Arial", 15))
display.place(relx = 0.5, rely = 0.2, anchor = CENTER)
entry = Text(root, bg = "cyan", font = ("Sylfaen", 10), height = 10, wrap = WORD, width = 40, padx = 10, pady = 10, bd = 0)
entry.place(relx = 0.5, rely = 0.5, anchor = CENTER)
root.mainloop()