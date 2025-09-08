# Simple weight conversion

weight = float(input("Enter your weight: "))
unit = input("Is the weight in kg or lbs? (kg/lbs): ")

if unit == "kg":
    weight = weight * 2.205
    unit = "lbs"
    print(f"Your weight is: {round(weight, 1)} {unit}.")
elif unit == "lbs":
    weight = weight / 2.205
    unit = "kgs"
    print(f"Your weight is: {round(weight, 1)} {unit}.")
else:
    print(f"{unit} is not valid!")

