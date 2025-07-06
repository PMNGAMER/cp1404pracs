
"""import operator
data = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}


# Use itemgetter from operator module to sort by value
sorted_items = sorted(data.items(), key=operator.itemgetter(1), reverse=True)

# Print in aligned format
for name, value in sorted_items:
    print(f"{name:<12} = {value}")


#Desired OUTPUT
#Bob         = 612
#Xavier      = 80
#Chantanelle = 9
#Derek       = 7
"""

def main():
    data = ["name", "Alice", "age", "25", "country", "Singapore"]
    print(list_to_dict(data))


def list_to_dict(pairs):
    result = {}
    for i in range(0, len(pairs) - 1, 2):
        key = pairs[i]
        value = pairs[i + 1]
        result[key] = value
    return result
main()

