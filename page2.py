from tkinter import *
import tkinter as tk
from tkinter import colorchooser
from PIL import ImageTk, Image
conversion_table = ['0', '1', '2', '3', '4', '5',
                    '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def decTohex(n):
    if (n <= 0):
        return ''
    remainder = n % 16
    return decTohex(n//16)+conversion_table[remainder]


def convertRGBtoHex(R, G, B):

    if ((R >= 0 and R <= 255) and
        (G >= 0 and G <= 255) and
            (B >= 0 and B <= 255)):
        hexCode = '#'
        r1 = int(R)
        g1 = int(G)
        b1 = int(B)
        hexCode = hexCode + decTohex(r1)
        hexCode = hexCode + decTohex(g1)
        hexCode = hexCode + decTohex(b1)
        return hexCode

    else:
        return "-1"


def bilinearinterarea(l1, l2, w1, w2):
    area1 = l1 * w1
    area2 = l2 * w1
    area3 = l1 * w2
    area4 = l2 * w2
    arrarea = [area1, area2, area3, area4]
    return arrarea


def bilinearinter1(l1, l2, w1, w2, point1=[], point2=[], point3=[], point4=[]):
    newpoint = []
    area = bilinearinterarea(l1, l2, w1, w2)
    color_code = []
    i = 0
    while (i < 3):
        np = point1[i]*area[3] + point2[i]*area[2] + \
            point3[i]*area[1]+point4[i]*area[0]
        newpoint.append(np)
        i = i+1
    color_code.append(newpoint)
    color_code.append(convertRGBtoHex(newpoint[0], newpoint[1], newpoint[2]))
    return color_code


def choose_color1():
    color_code = colorchooser.askcolor(title="Choose color")
    global point1
    point1 = color_code[0]
    button1.config(bg=color_code[1],
                   text="Color Value :{}".format(color_code[0]), bd=1)
    print(point1)
    print(color_code)
    return point1


def choose_color2():
    color_code = colorchooser.askcolor(title="Choose color")
    global point2
    point2 = color_code[0]
    button2.config(bg=color_code[1],
                   text="Color Value :{}".format(color_code[0]), bd=1)
    print(point2)
    print(color_code)
    return point2


def choose_color3():
    color_code = colorchooser.askcolor(title="Choose color")
    global point3
    point3 = color_code[0]
    button3.config(bg=color_code[1],
                   text="Color Value :{}".format(color_code[0]), bd=1)
    print(point3)
    print(color_code)
    return point3


def choose_color4():
    color_code = colorchooser.askcolor(title="Choose color")
    global point4
    point4 = color_code[0]
    button4.config(bg=color_code[1],
                   text="Color Value :{}".format(color_code[0],), bd=1)
    print(point4)
    print(color_code)
    return point4


def choose_color5():
    c = bilinearinter1(0.57, 0.43, 0.5, 0.5, point1, point2, point3, point4)
    print(c)
    T.insert(END, c[1])
    x = "(%s ,%d ,%d)" % (int(c[0][0]), int(c[0][1]), int(c[0][2]))
    button5.config(bg=c[1], text=x, bd=1)


root = Tk()
button1 = Button(root, text="First Color",
                 height=8, width=18, command=choose_color1, bd=10, highlightbackground="black", highlightthickness=2)
button2 = Button(root, text="Second Color",
                 height=8, width=18, command=choose_color2, bd=10, highlightbackground="black", highlightthickness=2)
button3 = Button(root, text="Third Color",
                 height=8, width=18, command=choose_color3, bd=10, highlightbackground="black", highlightthickness=2)
button4 = Button(root, text="Fourth Color",
                 height=8, width=18, command=choose_color4, bd=10, highlightbackground="black", highlightthickness=2)
button5 = Button(root, text="Goal Color", height=8,
                 width=18, command=choose_color5, bd=10, highlightbackground="black", highlightthickness=2)
la = Label(root, text='', height=10, width=16)
la["bg"] = "#d9d1c3"
la.grid(row=0, column=0)
button1.grid(row=0, column=1)
button2.grid(row=0, column=3)
button3.grid(row=2, column=1)
button4.grid(row=2, column=3)
button5.grid(row=1, column=2, pady=7, padx=20)

T = Text(root, height=2, width=20)
T.grid(row=1, column=6)
root.geometry("800x533")
root["bg"] = "#d9d1c3"
root.mainloop()
