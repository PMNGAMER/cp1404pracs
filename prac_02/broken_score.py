"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
while score > 0 and score <= 100:
    if score > 90:
        print("Excellent")
    elif score >= 50:
        print("Pass")
    else:
        print("Fail")
    score = float(input("Enter score: "))
print("Invalid score")