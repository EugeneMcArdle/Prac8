from taxi import Taxi

def main():
    myTaxi = Taxi("Prius 1", 100, 1.2)

    myTaxi.drive(40)
    print(myTaxi)
    print("Current Fare: ${:.2f}".format(myTaxi.get_fare()))
    myTaxi.start_fare()
    myTaxi.drive(100)
    print(myTaxi)
    print("Current Fare: ${:.2f}".format(myTaxi.get_fare()))

main()
