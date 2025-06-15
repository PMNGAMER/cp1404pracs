"""names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))

name_to_remove = input("Who do you want to remove? (Press Enter to stop): ")
while name_to_remove != "":
    if name_to_remove in names:
        names.remove(name_to_remove)
        print(f"{name_to_remove} removed.")
    else:
        print(f"{name_to_remove} not found in the list.")
    print("Remaining names:", ", ".join(names))
    name_to_remove = input("Who do you want to remove? (Press Enter to stop): ")"""

#Try and Except Style

"""names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))

name_to_remove = input("Who do you want to remove? (Press Enter to stop): ")
while name_to_remove != "":
    try:
        names.remove(name_to_remove)
        print(f"{name_to_remove} removed.")
    except ValueError:
        print(f"{name_to_remove} not found in the list.")
    print("Remaining names:", ", ".join(names))
    name_to_remove = input("Who do you want to remove? (Press Enter to stop): ")"""


"""def main():
    numbers = get_numbers()
    squared = square_numbers(numbers)
    display_numbers(squared)
def get_numbers():
    number = input("Enter Numbers: ")
    return [number for number in number.split(",")]

def square_numbers(numbers):
     return [number ** 2 for number in numbers]

def display_numbers(numbers):
    return sorted(numbers)

main()"""
#the one above is still wrong

from operator import itemgetter

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612],['Chantanelle', 9]]

name_width = max(len(pair[0]) for pair in data)
score_width = max(len(str(pair[1])) for pair in data)

data = sorted(data, key=itemgetter(1), reverse=True)

for pair in data:
    name, score = pair
    print(f"{name:{name_width}} = {score:{score_width}}")







