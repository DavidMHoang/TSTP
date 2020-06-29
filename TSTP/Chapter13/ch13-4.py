class Horse():
    def __init__(self, rider):
        self.rider = rider


class Rider():
    def __init__(self, rider, horse):
        self.rider = rider
        self.horse = horse


horse = Horse("Horse")
bob = Rider("Bob", horse)

print(bob.horse.rider)

