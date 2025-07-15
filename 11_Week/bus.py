class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = 0

    def on_bus(self):
        if self.passengers < self.max_passengers:
            self.passengers += 1
            print("A passenger got on. Seats left:", self.max_passengers - self.passengers)
        else:
            print("I'm sorry, there isn't enough space.")

    def get_off_bus(self):
        if self.passengers > 0:
            self.passengers -= 1
            print("A passenger got off. Passengers now:", self.passengers)
        else:
            print("The bus is already empty")




my_bus = Bus(3)

my_bus.on_bus()
my_bus.on_bus()
my_bus.on_bus()
my_bus.on_bus()


my_bus.get_off_bus ()
my_bus.get_off_bus ()
my_bus.get_off_bus ()
my_bus.get_off_bus ()


