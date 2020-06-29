class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def calculate_perimeter(self):
        return ((2*self.width) + (2*self.length))

class Square():
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return (self.side*4)

    def change_size(self, change):
        self.side += change


rect = Rectangle(10, 20)
sq = Square(10)

print(rect.calculate_perimeter())
print(sq.calculate_perimeter())
sq.change_size(-6)
print(sq.calculate_perimeter())
