class CoffeeMaker:
    def make(self):
        print("Your coffee is in process....")


class HotWaterProvider(CoffeeMaker):
    def __init__(self, water=True):   
        self.water = water

    def process_request(self):
        if self.water:
            print("The CoffeeMaker can also provide hot water.")
        else:
            print("No hot water available.")



coffewater = HotWaterProvider()


coffewater.process_request()  
coffewater.make()
