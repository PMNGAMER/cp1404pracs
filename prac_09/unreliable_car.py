from prac_09.car import Car
import random

class UnreliableCar(Car):
    """An UnreliableCar that may not drive every time."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car based on reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            print(f"{self.name} failed to start!")
            return 0
