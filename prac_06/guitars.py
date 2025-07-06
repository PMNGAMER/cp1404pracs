from guitar import Guitar

def main():
    """Program to let the user input guitar details and display them nicely."""
    guitars = []

    print("My guitars!")

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:,.2f} added.\n")
        name = input("Name: ")

# Comment out this test data section to match output shown in github
        #guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
        #guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

main()