FILENAME = "wimbledon.csv"

def main():
    data = read_wimbledon_data(FILENAME)
    champions_to_wins, champion_countries = process_wimbledon_data(data)
    display_champions(champions_to_wins)
    display_countries(champion_countries)


def read_wimbledon_data(filename):
    """Read the Wimbledon CSV and return data as list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]
    return [line.strip().split(",") for line in lines]


def process_wimbledon_data(data):
    """Process the data into a dict of champions and a set of countries."""
    champions_to_wins = {}
    champion_countries = set()

    for row in data:
        country = row[1]
        champion = row[2]
        champion_countries.add(country)
        if champion in champions_to_wins:
            champions_to_wins[champion] += 1
        else:
            champions_to_wins[champion] = 1

    return champions_to_wins, champion_countries


def display_champions(champions_to_wins):
    """Display champions and how many times they have won."""
    print("Wimbledon Champions:")
    for champion, wins in sorted(champions_to_wins.items()):
        print(f"{champion:20} {wins}")


def display_countries(countries):
    """Display all countries in alphabetical order."""
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

main()