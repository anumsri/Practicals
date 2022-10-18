def main():
    email_to_name = {}
    email = input("Enter Email: ")
    while email != "":
        name = get_name_from_email(email)
        name_check = input(f"Is your name {name}? (Y/n) ")
        if name_check.upper() != "Y" and name_check != "":
            name = input("Enter Name: ")
        email_to_name[email] = name
        email = input("Enter Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
