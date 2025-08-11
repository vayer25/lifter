#new class person
class Person:
    def __init__(self, name):
        self.name = name

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []  

    def on_bus(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} got on. Seats left: {self.max_passengers - len(self.passengers)}")
        else:
            print("I'm sorry, there isn't enough space.")

    def get_off_bus(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} got off. Passengers now: {len(self.passengers)}")
        else:
            print(f"{person.name} is not on the bus.")


my_bus = Bus(3)


p1 = Person("Alice")
p2 = Person("Bob")
p3 = Person("Charlie")
p4 = Person("David")


my_bus.on_bus(p1)
my_bus.on_bus(p2)
my_bus.on_bus(p3)
my_bus.on_bus(p4)  


my_bus.get_off_bus(p2)
my_bus.get_off_bus(p4)  
