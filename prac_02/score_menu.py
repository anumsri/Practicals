MENU = """
1 - Get Valid Score
2 - Print Result
3 - Print stars
4 - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "1":
            score = get_valid_score()
        elif choice == "2":
            print(determine_score(score))
        elif choice == "3":
            print_asterisk(score)


def get_valid_score():
    score = float(input("Enter score: "))
    while score == "":
        print("Invalid Score")
        score = float(input("Enter score: "))
    return score


def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 50:
        return "Passable"
    elif score > 90:
        return "Excellent"
    else:
        return "Bad"


def print_asterisk(score):
    return "*" * len(score)


main()
