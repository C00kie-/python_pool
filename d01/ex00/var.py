
#-- pseudo code!--
def fill() :
    for element in my_var():
        print element, "est de type", type(element) # en gros (avec un truc comme printf)

def my_var() :
    a = 42
    b = "42"
    c = "quarante deux"
    e = 42.0
    f = bool(True) #-- pour expliciter le type
    g = [42]
    h = { '42' : 42}
    i = (42,)
    fill()

if __name__ == "__main__" : #ça c'est bon au moins c'est le main
    my_var()
