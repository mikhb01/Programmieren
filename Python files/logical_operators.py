# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be TRUE
#                     and = both conditions must be TRUE
#                     not = inverts the condition (not FALSE, not TRUE)

# temp = 25
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled!")
# else:
#     print("The outdoor event is still scheduled!")

temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")
# elif temp < 28 and temp > 0 and is_sunny:
#     print("It is warm outside")
#     print("It is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside")
    print("It is sunny")
    