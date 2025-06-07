import random

print(random.randint(5, 20))  # line 1 ANY INTEGER BETWEEN 5 and 20
print(random.randrange(3, 10, 2))  # line 2 ANY INTEGER WITH A STEP OF 2 FROM 3 to 10
print(random.uniform(2.5, 5.5))  # line 3 ANY NUMBER FROM 2.5 to 5.5

"""What did you see on line 1?
What was the smallest number you could have seen, what was the largest?
Smallest is 5 and Largest is 20
What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Smallest is 3 and Largest is 9
Could line 2 have produced a 4?
No.

What did you see on line 3?
What was the smallest number you could have seen, what was the largest?
Smallest is close to 2.5 and Largest is close to 5.5
Write code, not a comment, to produce a random number between 1 and 100 inclusive."""
print(random.randint(1, 100))
