#using callback and buttons
#http://effbot.org/zone/tkinter-callbacks.htm

import maintenance

from tkinter import *

fenetre = Tk()

cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
cadre.pack(fill=BOTH)

message = Label(cadre, text="ALBERT")
message.pack(side="top")


#a = Button(cadre, text="a button", command = Button.quit)
#a.pack()

def callback():
    maintenance.manufacturer()
    return("ok")

b = Button(cadre, text="ain't working, please fix the bug", command=callback)
b.pack()



#liste des boissons

message = Label(cadre, text="Hoho choix des boissons")
message.pack()

liste = Listbox(cadre)
liste.pack()

#linker les elements de cette liste a nos beverages
liste.insert(END, "Coffee")
liste.insert(END, "Tea")
liste.insert(END, "Capuccino")
liste.insert(END, "Chocolate")
liste.insert(END, "Milk")



if __name__ == '__main__':
    fenetre.mainloop()

    #une commande pour terminer le programme auto
