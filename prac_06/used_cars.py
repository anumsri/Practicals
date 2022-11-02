"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    my_car.add_fuel(20)
    my_car.drive(115)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    taxi = Car("Car", 100)
    taxi.add_fuel(20)
    print(taxi.fuel)
    taxi.drive(115)
    print(taxi)


main()