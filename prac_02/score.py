"""
CP1404/CP5632 - Practical
Program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    score_status = assess_score(score)
    print(score_status)


def assess_score(score: float):
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
