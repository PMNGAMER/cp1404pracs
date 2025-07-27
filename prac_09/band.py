"""Band class for CP1404"""

class Band:
    """A Band class that has a name and a collection of musicians."""

    def __init__(self, name):
        """Initialize the Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a Musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the Band and its Musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def play(self):
        """Return a string of what each musician in the band is playing."""
        return "\n".join(musician.play() for musician in self.musicians)
