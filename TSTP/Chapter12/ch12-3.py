class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return (.5 * self.base * self.height)

triangle = Triangle(10, 20)
print(triangle.area())
