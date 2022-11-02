from prac_06.guitar import Guitar


def guitar_test():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    another = Guitar("Another Guitar", 2012, 1512.9)
    print(f"{guitar.name} get_age() - Expected {100}. Got {guitar.get_age()}")
    print(f"{another.name} get_age() - Expected {9}. Got {another.get_age()}")

    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")


guitar_test()
