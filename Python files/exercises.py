# Exerise 1 Rectangle Area Calc
# Formel: L(änge) * B(reite) [L(ength) * W(idth)]

# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
# area = length * width

# print(f"The area of the recangle is {area}cm²")

#Exercise 2 Shopping cart program

# item = input("What item would you like to buy?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many would you like?: "))
# total = price * quantity

# print(f"You have bought {quantity} x {item}/s")
# print(f"Your total is: €{total}")

# Exercise 3 Circumference of a circle
# import math

# # Formel = U(mfang) = 2 * pi * r(adius) [C(ircumference) = 2 * pi * r(adius)]

# radius = float(input("Enter the radius of a circle: "))

# circumference = 2 * math.pi * radius

# print(f"The circumference is: {round(circumference, 2)}cm.")

#Exercise 4 Area of a circle
#Formel A(rea) = pi * r(adius)²

# import math

# radius = float(input("Enter the radius of a circle: "))

# area = math.pi * pow(radius, 2)

# print(f"The area of the circle is {round(area, 2)}cm²")


# Exercise 5 Hypothenus of a triangle
# Formel: a² + b² = c² / (sqrt of a² + b²) = c

import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side c = {round(c, 2)}")