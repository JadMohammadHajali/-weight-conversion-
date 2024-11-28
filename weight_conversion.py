""" weight conversion project

    used to conversion your weight to kilograms or pounds
"""

weight = float(input("Enter Your Weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit in ('k','K'):
    weight = weight * 2.205
    units = "Lbs."
    print(f"Your weight is {round(weight,1)} {units}")
elif unit in('l','L'):
    weight = weight / 2.205
    units = "Kgs."
    print(f"Your weight is {round(weight, 1)} {units}")
else:
    print(f"{unit} was not valid")
