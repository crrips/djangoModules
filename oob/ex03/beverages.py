class HotBeverage:
    def __init__(self):
        self.price = 0.30
        self.name = "hot beverage"
        self.descr = "Just some hot water in a cup."

    def description(self) -> str:
        return self.descr

    def __str__(self):
        return f"name: {self.name}\nprice: {self.price}\ndescription: {self.descr}"


class Coffee(HotBeverage):
    def __init__(self):
        self.price = 0.40
        self.name = "coffee"
        self.descr = "A coffee, to stay awake."


class Tea(HotBeverage):
    def __init__(self):
        self.price = 0.30
        self.name = "tea"
        self.descr = "Just some hot water in a cup."


class Chocolate(HotBeverage):
    def __init__(self):
        self.price = 0.50
        self.name = "chocolate"
        self.descr = "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    def __init__(self):
        self.price = 0.45
        self.name = "cappuccino"
        self.descr = "Un po' di Italia nella sua tazza!"


if __name__ == '__main__':
    print(HotBeverage())
    print(Coffee())
    print(Tea())
    print(Chocolate())
    print(Cappuccino())
