# ch3_2.py
from tkinter import *

window = Tk()
window.title("ch3_2")
lab1 = Label(window, text="明志科技大学",
            bg="lightyellow",
            width=15)
lab2 = Label(window, text="长庚大学",
            bg="lightgreen",
            width=15)
lab3 = Label(window, text="长庚科技大学",
            bg="lightblue",
            width=15)
lab1.pack(side=BOTTOM)
lab2.pack(side=BOTTOM)
lab3.pack(side=BOTTOM)

window.mainloop()
