"""
Program that utilises a menu to perform actions related to the users score.
"""
import random

MENU = """
1. Re-enter name
2. Receive greeting
3. Receive secret name
4. Quit
"""


def main():
    """Create a menu."""
    name = get_name()
    print(MENU)
    choice = str(input(">>> "))
    while choice != "4":
        if choice == "1":
            name = get_name()
        elif choice == "2":
            print_greeting(name)
        elif choice == "3":
            print_secret_name(name)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = str(input(">>> "))
    print("Quitting program.")


def get_name():
    """Get the users name."""
    name = input("Input your name: ")
    while name == "":
        print("Invalid name.")
        name = input("Input your name: ")
    return name


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