from guitar import Guitar

def main():
    """Test the get_age and is_vintage methods of the Guitar class."""
    CURRENT_YEAR = 2025

    # Create test guitars
    guitar_1 = Guitar("Gibson L-5 CES", 1925, 16035.40)
    guitar_2 = Guitar("Another Guitar", 2016, 1000)

    # Expected results
    expected_age_1 = CURRENT_YEAR - 1925
    expected_age_2 = CURRENT_YEAR - 2016

    # Test get_age()
    print(f"{guitar_1.name} get_age() - Expected {expected_age_1}. Got {guitar_1.get_age()}")
    print(f"{guitar_2.name} get_age() - Expected {expected_age_2}. Got {guitar_2.get_age()}")

    # Test is_vintage()
    print(f"{guitar_1.name} is_vintage() - Expected True. Got {guitar_1.is_vintage()}")
    print(f"{guitar_2.name} is_vintage() - Expected False. Got {guitar_2.is_vintage()}")

main()