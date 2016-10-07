

class Intern :
    #si rien dedans peut mettre pass

    def __init__(self, str="My name? I'm nobody, an intern, I have no name."):
        self.name = str
        pass

    def __str__(self):
        return "mon nom est " + str(self.name)

    class Coffee :
        def __str__(self):
            return("This is the worst coffee you ever tested.")
#   intern.work() => work(self=intern)
    def work(self):
        raise Exception("I'm just an intern, I can't do that")

    def make_coffee(self):
        return(self.Coffee())


if __name__ == '__main__':
    inter1 = Intern('Rocky')
    try:
        inter1.work()
    except Exception as e:
        print(e)
    print('inter1.name : ')
    print(inter1.name)

    print('inter1 : ')
    print(inter1)

    print(inter1.Coffee())#pourquoi ca print <class '__main__.Intern.Coffee'>
#parce que necessite instancie la classe
#    Capuccino = Intern.Coffee()

    print(inter1.make_coffee())

    inter2 = Intern('Mark')
    print(inter2)
    inter2.make_coffee()
