password = input("Enter Password: ")
while len(password) < 6:
    password = input("Enter Password: ")
print("*" * len(password))
