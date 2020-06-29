class Square():
    square_list = []

    def __init__(self, s):
        self.side = s
        self.square_list.append(self.side)

    def __repr__(self):
        return ("""{} by {} by {} by {}
              """.format(self.side,
                         self.side,
                         self.side,
                         self.side))


sq1 = Square(20)
sq2 = Square(30)
sq3 = Square(5)

print(Square.square_list)
print(sq1)
print(sq2)
print(sq3)
