

class Intern :
    #si rien dedans peut mettre pass

    def __init__(self, str='valeur par default'):
        self.name = str
        pass

    def __str__(self):
        return self.Name

    class Coffee :
        def __str__(self):
            return("This is the worst coffee you ever tested.")
#   intern.work() => work(self=intern)
    def work(self):
        raise Exception("I'm just an intern, I can't do that")





if __name__ == '__main__':
    number = int()
    inter = Intern('Rocky')
    try:
        inter.work()
    except Exception as e:
        print(e)
