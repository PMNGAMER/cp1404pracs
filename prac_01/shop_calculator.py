num_of_items = int(input("Number of Items: "))
while num_of_items < 0:
    print("Invalid Number of Items !")
    num_of_items = input("Number of Items: ")

total_price = 0

for i in range(num_of_items):
    price = float(input("Price of Item: "))
    total_price += price

if total_price > 100:
    discounted_price = total_price * 0.1
    total_price = total_price - discounted_price

print(f"Total Price for {num_of_items} items is ${total_price:.2f}")