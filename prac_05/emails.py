def get_name_from_email(email):
    """Extract a guessed name from an email address."""
    prefix = email.split('@')[0]
    parts = prefix.replace('.', ' ').split()
    return ' '.join(parts).title()


def main():
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        guessed_name = get_name_from_email(email)
        confirmation = input(f"Is your name {guessed_name}? (Y/n) ").lower()
        if confirmation not in ('', 'y'):
            name = input("Name: ")
        else:
            name = guessed_name
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
