MIN_LENGTH = 1
MAX_LENGTH = 6


def main():
    password = get_password()
    while len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        print("Invalid password")
        password = get_password()
    print_asterisk(password)


def print_asterisk(password):
    print("*" * len(password))


def get_password():
    password = input("Enter Password: ")
    return password


main()