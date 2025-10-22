# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and imutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = ["apple", "orange", "banana", "coconut"] # List
# fruits = {"apple", "orange", "banana", "coconut"} # Set
fruits = ("apple", "orange", "banana", "coconut") # Tuple

## usable with all three ##
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)


## usable with List ##

# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("pineapple"))

## Usable with Set ##
# fruits.add("pineapple")
# fruits.remove("orange")
# fruits.pop()
# fruits.clear()


## Usable with Tuple ##
# print(fruits.index("apple"))
# print(fruits.count("coconut"))

for fruit in fruits:
    print(fruit)

# for fruit in fruits:
#     print(fruit)