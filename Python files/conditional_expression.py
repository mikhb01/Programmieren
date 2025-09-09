# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                           Print or assign one of two values based on conditions
#                           X if condition else Y

num = 6

# print("Positive" if num > 0 else "Negative")

# result = "EVEN" if num % 2 == 0 else "ODD"
# print(result)

a = 6
b = 7

max_num = a if a > b else b
min_num = a if a < b else b

# print(max_num)
# print(min_num)

age = 25

status = "Adult" if age >= 18 else "Child"

print(status)