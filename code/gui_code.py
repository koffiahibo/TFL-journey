import tkinter as tk
from tkinter import ttk
from commands import *
window1 = tk.Tk()
window1.geometry("500x500")
from_entry = ttk.Label(window1)
from_entry.config(text= "Your TFL Journey planner")

def arb1():
    print("Your TFL Journey Planner")

plan_button = ttk.Button(window1)
plan_button.config(text = "Plan route", command=arb )
plan_button.pack()

to_entry = ttk.Entry(window1)
from_entry.pack()
to_entry.pack()


window1.mainloop()