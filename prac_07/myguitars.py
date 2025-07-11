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


def main():
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    print("These are the guitars in original order:")
    display_guitars(guitars)

    print("\nThese are the guitars sorted by year:")
    guitars.sort()
    display_guitars(guitars)


main()
