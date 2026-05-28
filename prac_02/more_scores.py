"""
Program to assess randomly generated scores.
"""

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














