class CoffeeMaker:
    def make(self):
        print("Please take your coffee")


class HotWaterProvider(CoffeeMaker):
    def __init__(self, water=True):   
        self.water = water

    def process_request(self):
        if self.water:
            print("Please take your hot water.")
        else:
            print("No hot water available.")


class MilkFrother:
    def __init__(self, frother=True):  
        self.frother = frother

    def processing(self):
        if self.frother:
            print("Please take you frothy coffee.")
        else:
            print("It is a regular coffee.")


class CoffeeMachine(CoffeeMaker, HotWaterProvider, MilkFrother):
    def __init__(self, water=True, frother=True):
        HotWaterProvider.__init__(self, water)  
        MilkFrother.__init__(self, frother) 



machine = CoffeeMachine(water=True, frother=True)

machine.make()          
machine.process_request() 
machine.processing()
