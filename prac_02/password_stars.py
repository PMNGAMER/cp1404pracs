MIN_LENGTH = 6

def main():
    password = get_password(MIN_LENGTH)
    print_asterisks(password)
def get_password(MIN_LENGTH):
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password is too short! Must be at least {MIN_LENGTH} characters.")
        password = input("Enter a password: ")
    return password


def print_asterisks(password):
    print("*" * len(password))

main()

