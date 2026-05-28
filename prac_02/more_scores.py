"""
Program to assess randomly generated scores.
"""
import random

FILENAME = "results"
LOWEST_SCORE = 0
HIGHEST_SCORE = 100


def main():
    """Write randomly generated scores to .txt file."""
    number_of_scores = get_number_of_scores()
    create_empty_text_file(FILENAME)
    for _ in range(number_of_scores):
        random_score = random.randint(LOWEST_SCORE, HIGHEST_SCORE)
        score_status = assess_score(random_score)
        score_message = f"{random_score} is {score_status}\n"
        append_to_text_file(FILENAME, score_message)
        print(score_message)
    print(f"An assessment of {number_of_scores} random scores has been printed to {FILENAME}.txt")


def create_empty_text_file(filename: str):
    """Create an empty file filename.txt"""
    with open(filename + ".txt", "w", encoding="utf-8") as f:
        f.write("")


def append_to_text_file(filename: str, message: str):
    """Append a string to filename.txt."""
    with open(filename + ".txt", "a", encoding="utf-8") as f:
        f.write(message)


def get_number_of_scores() -> int:
    """Get a positive integer number of scores."""
    number_of_scores = float(input("Number of scores: "))
    while number_of_scores < 1 or number_of_scores % 1 > 0:
        print("Invalid number of scores (must be a positive integer).")
        number_of_scores = float(input("Number of scores: "))
    return int(number_of_scores)


# TODO: Import this function from score.py
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


main()
