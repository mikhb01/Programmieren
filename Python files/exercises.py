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

# import math

# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))

# c = math.sqrt(pow(a, 2) + pow(b, 2))

# print(f"Side c = {round(c, 2)}")


# Exercise 6 validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

username.find(" ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")