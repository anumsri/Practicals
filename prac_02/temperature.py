"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = int(input("Enter Number of Items: "))


def celsius_conversion():
    global fahrenheit
    fahrenheit = celsius * 9.0 / 5 + 32


def farenheit_conversion():
    global fahrenheit
    fahrenheit = float(input("Farenheit: "))


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        celsius_conversion()
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        farenheit_conversion()
        celsius = 5 / 9.0 * (fahrenheit - 32)
        print("Result: {:.2f} F".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
