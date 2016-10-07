

class HotBeverage :


    def __init__(self, string="default name"): #valeur de name par default
        # self.name = string
        self.name = "Hot Beverage"
        self.price = "0.30"

    def __str__(self):
        #return(str(self.name))
        string = "name : {name}\nprice : {price}\ndescription : {desc}"
        return(string.format(name = self.name, price = self.price, desc = self.description()))


    def description(self):
        return("just some hot water in a cup")

class Coffee(HotBeverage):
    def __init__(self): #valeur de name par default
        # self.name = string
        self.name = "coffee"
        self.price = "0.40"

    def description(self):
        return("it's a infusion of cafein")

class Tea(HotBeverage):
    def __init__(self): #valeur de name par default
        # self.name = string
        super().__init__()
        self.name = "tea"

    def description(self):
        return("it's a infusion of thein")

class Chocolate(HotBeverage):
    def __init__(self): #valeur de name par default
        # self.name = string
        self.name = "Chocolate"
        self.price = "0.50"

    def description(self):
        return("it's milk and chocolate")


if __name__ == '__main__':
    HB = HotBeverage("coffee")
    print(HB)
    print(HB.price)

    CC = Coffee()
    print(CC)
    Cacao = Chocolate()
    print(Cacao)
    Tee = Tea()
    print(Tee)
