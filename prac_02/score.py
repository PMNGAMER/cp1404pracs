"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

import random
def main():
    score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(result)

    random_score = random.randint(0, 100)
    print(f"Generate Random Score: {random_score}")
    random_result = determine_score_result(random_score)
    print(random_result)



def determine_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()