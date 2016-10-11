from tkinter import *

fenetre = Tk()

cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
cadre.pack(fill=BOTH)

message = Label(cadre, text="Notre fenêtre")
message.pack(side="top")


a = Button(cadre, text="a button", command = Button.quit)
a.pack()

def callback():
    print("clicked!")
    return("ok")

b = Button(text="click me", command=callback)
b.pack()



if __name__ == '__main__':
    fenetre.mainloop()

    #une commande pour terminer le programme auto
