import beverages

class CoffeeMachine:

    def __init__(self):
        self.name = "a machine !!!"

    def __str__(self):
        return("I'm " + self.name)

    class BrokenMachineException(Exception):#comment on construit une exception??
        message == "This machine as not be repaired"

    def repair(self):
        pass
        #comment remettre le compteur de la machine a 0?

    def serve(Coffee):
        #comment gerer le cas de l'obsolescence?
        #comment faire un retour une fois sur deux/
        t++
        return(Coffee())
        #or
        #return(EmptyCup())
        if
        #bloc de service
        raise BrokenMachineException as b:
            "This machine need a reparation"


class EmptyCup(beverages.HotBeverage):
    def __str__(self):
        self.name = "empty cup"
        self.prix = "0.90"
        return(self.name)

    def description(self):
        return("An empty cup? Gimme my money back!")






if __name__ == '__main__':
    test = CoffeeMachine()
    cup = EmptyCup()# place le nom au bon endroit
    print(test)
    print(cup)
