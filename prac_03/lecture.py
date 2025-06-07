def main():
    """Read a file and print only the lines that start with '#'."""
    filename = input("Enter the file name: ")

    try:
        with open(filename, "r") as file:
            for line in file:
                if line.startswith("#"):
                    print(line.rstrip())  # remove trailing newline
    except FileNotFoundError:
        print("File not found.")

main()
