import math

class Circle:
    def __init__(self, radio):
        self.radio = radio

    def get_area(self):
        return int(math.pi * self.radio ** 2)

circle = Circle(1)
area = circle.get_area()

print(f"The area of the circle is: {area}")