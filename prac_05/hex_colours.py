
CODE_TO_NAME = {"ABSOLUTE ZERO": "#0048ba", "ACID GREEN": "#bobf1a", "ALICEBLUE": "#f0f8ff",
                "ALIZARIN CRIMSON": "#e32636",
                "AMARANTH": "#e52b50", "AMBER": "#ffbf00", "AMETHYST": "#9966cc", "ANTIQUEWHITE": "#faebd7",
                "APRICOT": "#fbceb1", "AQUA": "#00fff"}
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")

hex_code = input("Enter a color: ").upper()
while hex_code != "":
    try:
        print(hex_code, "is", CODE_TO_NAME[hex_code])
    except KeyError:
        print("Invalid color")
    hex_code = input("Enter a color: ").upper()