"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    score_status = assess_score(score)
    print(f"User score {score} is {score_status}")
    if score_status == "Excellent":
        print("You get a prize!")
    random_score = random.randint(0, 100)
    random_score_status = assess_score(random_score)
    print(f"Random: {random_score} = {random_score_status}")


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
