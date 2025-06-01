MIN_LENGTH = 6

password = input("Enter a password: ")
while len(password) < MIN_LENGTH:
    print(f"Password is too short! Must be at least {MIN_LENGTH} characters.")
    password = input("Enter a password: ")

print("*" * len(password))