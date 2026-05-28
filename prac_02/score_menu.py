"""
Program that utilises a menu to perform actions related to the users score.
"""

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
            score_status = assess_score(valid_score)
            print(f"User score {valid_score} is {score_status}.")
        elif choice == "S":
            print_asterisks(int(valid_score))
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


def assess_score(score: float) -> str:
    """Return a score status based on input score."""
    if score > 100:
        score_status = "Invalid score"
    elif score >= 90:
        score_status = "Excellent"
    elif score >= 50:
        score_status = "Passable"
    elif score >= 0:
        score_status = "Bad"
    else:
        score_status = "Invalid score"
    return score_status


def print_asterisks(amount: int):
    """Print a row of *'s of length amount."""
    print("*" * amount)


main()
