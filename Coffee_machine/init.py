#https://openclassrooms.com/courses/apprenez-a-programmer-en-python/des-interfaces-graphiques-avec-tkinter
#https://www.tutorialspoint.com/python/tk_label.htm


from tkinter import *

fenetre = Tk()

champ_label = Label(fenetre, pady=12, bg="#800000", text="Hello, I'm Albert, your coffee machine today")

button_ok = Button(fenetre, text="Clic me", command=fenetre.quit)

v = StringVar() #a completer avec ligne de saisie, via le champ Entry

e = Entry(fenetre, textvariable=v)

v.set("a default value")

s = v.get()



ligneText = Entry(fenetre, textvariable=v, width=50)


if __name__ == '__main__':

    champ_label.pack()

    button_ok.pack()

    ligneText.pack()

    e.pack()

    fenetre.mainloop()
