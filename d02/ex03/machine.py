import beverages

class CoffeeMachine:

    def __init__(self):
        self.name = "a machine !!!"
        self.count = 0

    def __str__(self):
        return("I'm " + self.name)

    class EmptyCup(beverages.HotBeverage):
        def __str__(self):
            self.name = "empty cup"
            self.prix = "0.90"
            return(self.name)

        def description(self):
            return("An empty cup? Gimme my money back!")



    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This machine has not be repaired")


    def repair(self):
        self.count = 0

    def serve(self, beverage):
        if self.count > 10:
            raise self.BrokenMachineException()
        self.count += 1

        #comment faire un retour une fois sur deux/ utiliser la fonction random

        return(beverage)#parce passe en instance dans le main
        #or
        #return(self.EmptyCup())# parce que pas instancie dans le main instancie ici
        if:
        #bloc de service





if __name__ == '__main__':
    test = CoffeeMachine()
    cup = CoffeeMachine.EmptyCup()# place le nom au bon endroit
    print(test)
    print(cup)
    print(cup.description())
    try :
        test.serve(beverages.Coffee())#() parce que instance !!
    except CoffeeMachine.BrokenMachineException as e:
        print (e)
        test.repair()
