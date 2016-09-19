from silverServiceTaxi import SilverStarTaxi


def main():
    fancy_taxi = SilverStarTaxi("Limo", 100, 2)
    fancy_taxi.drive(10)
    print(fancy_taxi)
    print("Fancy Fare: ${:.2f}".format(fancy_taxi.get_fare()))

main()