user_name = input("Enter Name: ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")

get_choice = input("Enter Choice: ")
while get_choice != "Q":
    if get_choice == "H":
        print(f"Hello {user_name}")
    elif get_choice == "G":
        print(f"Goodbye {user_name}")
    else:
        print("Invalid Message")

    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

    get_choice = input("Enter Choice: ")
print("Finished.")
