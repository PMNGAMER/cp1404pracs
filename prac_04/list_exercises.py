numbers = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
enter_username = input("Enter your Username: ")
if enter_username in usernames:
    print("Access Granted")
else:
    print("Access Denied")
    enter_username = input("Enter your Username: ")
for i in range(5):
    number = int(input("Enter a Number:"))
    numbers.append(number)

print(f"The first number is: {numbers[0]}")
print(f"The Last number is: {numbers[-1]}")
print(f"The smallest number is: {min(numbers)}")
print(f"The Largest number is: {max(numbers)}")
print(f"The average of the numbers is: {sum(numbers)/len(numbers)}")


