#maintenance pour remplir la vitrine du distributeur de boissons
from tkinter import *

import beverages

manu = Tk()

cadre = Frame(manu)
cadre.pack()

text = Label(cadre, text="Hello I'm the guy who fill the machine with beverages")



def manufacturer():
    print("Hello I'm the guy who fill the machine with beverages")
    text.pack(fill=BOTH, side="top")

    b = Button(cadre, text="click here", command=cadre.quit)
    b.pack()

if __name__ == '__main__':
    manufacturer()
