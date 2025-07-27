from unreliable_car import UnreliableCar

def test_unreliable_car():
    """Test that UnreliableCar behaves according to its reliability."""
    test_runs = 1000

    # Test for high reliability (90%)
    reliable_car = UnreliableCar("ReliableCar", 10000, 90)
    success_count = 0
    for _ in range(test_runs):
        # Reset odometer and fuel to a large amount so we can measure only success
        before_odometer = reliable_car.odometer
        reliable_car.drive(1)
        if reliable_car.odometer > before_odometer:
            success_count += 1
    print(f"[ReliableCar] Drove successfully {success_count} out of {test_runs} times (expected ~900).")

    # Test for low reliability (30%)
    unreliable_car = UnreliableCar("UnreliableCar", 10000, 30)
    success_count = 0
    for _ in range(test_runs):
        before_odometer = unreliable_car.odometer
        unreliable_car.drive(1)
        if unreliable_car.odometer > before_odometer:
            success_count += 1
    print(f"[UnreliableCar] Drove successfully {success_count} out of {test_runs} times (expected ~300).")


test_unreliable_car()
