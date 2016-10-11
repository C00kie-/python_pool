#https://openclassrooms.com/courses/apprenez-a-programmer-en-python/des-interfaces-graphiques-avec-tkinter
#https://www.tutorialspoint.com/python/tk_label.htm



from tkinter import *

fenetre = Tk()

cadre = Frame(fenetre, width=768, height=576, borderwidth=2)

cadre.pack(fill=BOTH)

champ_label = Label(fenetre, pady=12, bg="#800000", text="Hello, I'm Albert, your coffee machine today")

button_ok = Button(fenetre, text="Clic me", command=fenetre.quit)

v = StringVar() #est une variable tkinter, est un constructeur, pour stockr une
# var qui va changer  en utilisant v.trace(mode, cbk) et get()


e = Entry(fenetre, textvariable=v)

v.set("a default value") #http://effbot.org/tkinterbook/variable.htm

#s = v.get()



ligneText = Entry(fenetre, textvariable=v, width=50)


if __name__ == '__main__':



    champ_label.pack()

    button_ok.pack()

    ligneText.pack()

    e.pack()

    fenetre.mainloop()
