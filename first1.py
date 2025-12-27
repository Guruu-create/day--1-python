name = input('Write your name: ')
color =input("Write your favourite color: ")
print(name + ' likes ' + color)


total_amount = 1000
balance_amount = 255
used_amount = total_amount - balance_amount
print(f"your used amount {used_amount}")


weight = int(input("Your weight: "))
unit = input("l(lbs) or k(kgs): ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"your weight {converted} in pounds.") 
else:
    converted = weight / 0.45
    print(f"your weight {converted} in kilos.") 

             