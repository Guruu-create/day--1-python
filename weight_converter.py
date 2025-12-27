weight = int(input("Your weight: "))
unit = input("l(lbs) or k(kgs): ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"your weight {converted} in pounds.") 
else:
    converted = weight / 0.45
    print(f"your weight {converted} in kilos.")