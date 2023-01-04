

# Authors : Mahmoud Mohamed Kassem and Seif el-din Ehab Abd el fattah


from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import colorchooser
root = tk.Tk()
root.geometry('750x700')
root.title("InterPolation")
root['bg'] = ['#dbd3c5']


def indicate():
    root.destroy()
    import page2


img = ImageTk.PhotoImage(Image.open("France-1.png"))
panel = Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
a = Label(root, text="Welcome in Interpolation System", font=("Bold", 25))
start_btn = tk.Button(text="Start in Interpolation", font=(
    "Bold", 25), command=indicate).place(x=200, y=400)
a.pack()
root.mainloop()
