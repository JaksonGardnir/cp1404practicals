"""
Get a password and print a row of asterisks of the same length as password.
"""


def main():
    """Get a password and print a row of *'s of the same length as password."""
    password = get_password()
    print_asterisks(password)


def get_password() -> str:
    """Get a password from the user."""
    password = input("Input password: ")
    while len(password) < 10:
        print("Password must be at least 10 characters long.")
        password = input("Input password: ")
    return password


def print_asterisks(password: str):
    """Print a row of *'s of the same length as password"""
    print("*" * len(password))


main()
