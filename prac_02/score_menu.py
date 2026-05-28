"""
Program that utilises a menu to perform actions related to the users score.
"""
import random

MENU = """
(G)et a valid score.
(P)rint result.
(S)how stars.
(Q)uit.
"""


def main():
    """Generate a menu to perform actions related to the users score."""
    valid_score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            valid_score = get_valid_score()
        elif choice == "P":
            pass
        elif choice == "S":
            pass
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Quitting program.")


def get_valid_score() -> float:
    """Get a valid score from the user."""
    valid_score = float(input("Input score: "))
    while valid_score < 0 or valid_score > 100:
        print("Invalid score (must be between 0 and 100 inclusive).")
        valid_score = float(input("Input score: "))
    return valid_score


def print_greeting(name):
    """Print a greeting to the user that includes their name."""
    length_of_greeting = 11 + len(name)  # len() gives the number of characters in the string.
    print_line(length_of_greeting)
    print(f"Greetings {name}!")
    print_line(length_of_greeting)


def print_secret_name(name):
    """Print a secret name according to the name input by the user."""
    randomised_name = list(name)
    random.shuffle(randomised_name)
    randomised_name = "".join(randomised_name)
    print(f"Your secret name is {randomised_name}\n")


def print_line(line_length):
    """Print a line of -'s of length line_length."""
    print("-" * line_length)


main()
