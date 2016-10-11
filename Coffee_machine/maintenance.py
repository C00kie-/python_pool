#maintenance pour remplir la vitrine du distributeur de boissons
from tkinter import *

import beverages

manu = Tk()

cadre = Frame(manu, width=768, height=576, borderwidth=1)
#cadre.pack(fill=BOTH)

text = Label(cadre, text="Hello I'm the guy who fill the machine with beverages")

def manufacturer():
    print("Hello I'm the guy who fill the machine with beverages")
    text.pack()


if __name__ == '__main__':
    manufacturer()
