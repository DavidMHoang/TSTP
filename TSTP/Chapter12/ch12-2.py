import math

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return (2 * math.pi * self.radius)

circle = Circle(10)
print(circle.area())
