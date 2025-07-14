from guitar import Guitar


def load_guitars(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display the list of guitars."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def get_new_guitars():
    """Prompt the user to enter new guitars and return a list of new Guitar objects."""
    new_guitars = []
    print("\nEnter new guitars (leave name blank to finish):")
    while True:
        name = input("Name: ")
        if name == "":
            break
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            guitar = Guitar(name, year, cost)
            new_guitars.append(guitar)
        except ValueError:
            print("Invalid input! Please enter numeric values for year and cost.")
    return new_guitars


def save_guitars(filename, guitars):
    """Write the list of guitars to the CSV file."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def main():
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    print("These are the guitars loaded from file:")
    display_guitars(guitars)

    new_guitars = get_new_guitars()
    guitars.extend(new_guitars)

    print("\nThese are all the guitars (including new ones):")
    guitars.sort()
    display_guitars(guitars)

    save_guitars(filename, guitars)
    print(f"\nGuitars saved to {filename}.")


main()
