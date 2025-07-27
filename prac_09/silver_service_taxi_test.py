from silver_service_taxi import SilverServiceTaxi


def test_silver_service_taxi():
    # Create a fancy taxi
    fancy_taxi = SilverServiceTaxi("Hummer", 200, fanciness=2)

    # Start a new fare and drive 18 km
    fancy_taxi.start_fare()
    fancy_taxi.drive(18)

    # Calculate fare
    fare = fancy_taxi.get_fare()

    print(fancy_taxi)
    print(f"Fare: ${fare:.2f}")

    assert round(fare, 2) == 48.78, f"Expected $48.78 but got ${fare:.2f}"


test_silver_service_taxi()
