"""display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>"""





def main():
    print("MENU:"
          "(G)et a valid score (must be 0-100 inclusive)"
          "\n(P)rint result"
          "\n(S)how stars"
          "\n(Q)uit")

    get_choice = input("Enter your Choice: ")
    while get_choice != "Q":
        if get_choice == "G":
            score = get_valid_score()
            print(f"Your score is {score}")
        elif get_choice == "P":
            result = determine_score_result()
            print(f"Your result is {result}")
        elif get_choice == "S":
            num_of_stars(score)
        else:
            print("Please Enter a Valid Letter.")
            get_choice = input("Enter your Choice: ")
    print("Farewell...")
def get_valid_score():
    score = int(input("Enter Score: "))
    while score > 100 or score < 0:
        print("Please Enter a valid Score.")
        score = int(input("Enter Score: "))
    return score

def determine_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def num_of_stars(score):
    print("*" * score)

main()






