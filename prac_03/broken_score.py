"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    #get score
    score = float(input("Enter score: "))
    get_score(score)


def get_score(score):
    #is it a valid score
    if score < 0 or score > 100:
        print("Invalid score")
    else: #judge each case
        if score < 50:
            print("Bad")
        if score >= 50 and score < 90:
            print("Passable")
        if score >= 90:
            print("Excellent")

main()