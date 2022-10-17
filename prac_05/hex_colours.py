
COLOUR_CODES = {"AbsoluteZero": "#0048ba", "Acid Green": "#b0bf1a",
                "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                "AliceBlue": "##f0f8ff", "AlizarinCrimson": "#e32636"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print(f"The code for {colour_name} is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ")