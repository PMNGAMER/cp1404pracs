from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A more fancy Taxi with higher fare and flagfall charge."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness  # use class var from Taxi

    def get_fare(self):
        """Return the fare including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return string representation with flagfall shown."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
