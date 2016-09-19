from taxi import Taxi

class SilverStarTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness

    def get_fare(self):
        base_fare = super().get_fare()
        total_fare = base_fare * self.fanciness + SilverStarTaxi.flagfall
        return total_fare
