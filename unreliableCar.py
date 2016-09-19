from random import randint
from taxi import Car

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        startingChance = randint(0,100)
        if startingChance < self.reliability:
            print("Yay! It started!")
            distance_driven = super().drive(distance)
        else:
            print("You turn the key and nothing happens")
            distance_driven = 0
        return distance_driven