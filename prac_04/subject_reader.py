"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_details = []
    with open(FILENAME) as input_file:
        for line in input_file:
            print(line)  # See what a line looks like
            print(repr(line))  # See what a line really looks like
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            print(parts)  # See what the parts look like (notice the integer is a string)
            parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
            print(parts)  # See if that worked
            print("----------")
            subject_details.append(parts)

    return subject_details

def display_subject_details(data):
    """Display subject details from the loaded data."""
    for subject_code, lecturer, student_count in data:
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")



main()