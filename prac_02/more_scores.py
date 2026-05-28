"""
Program to assess randomly generated scores.
"""
import random

def main():
    number_of_scores = float(input("Number of scores: "))
    while number_of_scores < 1 or number_of_scores % 1 > 0:
        print("Invalid number of scores (must be a positive integer).")
        number_of_scores = float(input("Number of scores: "))
    number_of_scores = int(number_of_scores)

    # Create an empty .txt file.
    with open("results.txt", "w") as f:
        f.write("")

    for i in range(number_of_scores):
        random_score = random.randint(0,100)
        score_status = assess_score(random_score)
        score_message = f"{random_score} is {score_status}"
        print(score_message)
        # Write string into .txt file.
        with open("results.txt", "a") as f:
            f.write(score_message + "\n")


# TODO: Import this function from score.py
def assess_score(score: float) -> str:
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










