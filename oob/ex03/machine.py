import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino


class CoffeeMachine:

    class EmptyCup(HotBeverage):
        def __init__(self):
            self.price = 0.90
            self.name = "empty cup"
            self.descr = "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            self.message = "This coffee machine has to be repaired."

    def __init__(self):
        self.count = 10

    def repair(self):
        self.count = 10
        print("The coffee machine has been repaired.")

    def serve(self, beverage: HotBeverage) -> HotBeverage:
        if (self.count <= 0):
            raise CoffeeMachine.BrokenMachineException
        self.count -= 1
        if random.randint(0, 5) == 0:
            return CoffeeMachine.EmptyCup()
        return beverage()
    

if __name__ == '__main__':
    machine = CoffeeMachine()
    for i in range(15):
        try:
            print(machine.serve(random.choice([Coffee, Tea, Chocolate, Cappuccino, HotBeverage])))
        except CoffeeMachine.BrokenMachineException as e:
            print(e.message)
            machine.repair()
