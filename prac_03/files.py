name = input("Enter Your Name: ")
file_out = open("name.txt", "w")
file_out.write(name)
file_out.close()

file_in = open("name.txt", "r")
stored_name = file_in.read()
file_in.close()
print(f"Hi {stored_name}!")

with open("numbers.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
    print(first_number + second_number)

with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        total += int(line)
    print(total)
