from unreliable_car import UnreliableCar

# Create UnreliableCar instances
car1 = UnreliableCar("Mostly Reliable", 100, 90)
car2 = UnreliableCar("Unreliable Junk", 100, 10)

# Try driving both cars multiple times
for i in range(5):
    print(f"\nAttempt {i+1}:")
    print(f"Before driving: {car1}")
    car1.drive(30)
    print(f"After driving: {car1}")

    print(f"Before driving: {car2}")
    car2.drive(30)
    print(f"After driving: {car2}")
