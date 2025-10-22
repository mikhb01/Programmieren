## 2D Collections

# fruits =        ["apple", "orange", "banana", "coconut"]
# vegetables =    ["celery", "carrots", "potatoes"]
# meats =         ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrrots", "potatoes"],
             ["chicken", "fish", "turkey"]]


# print(groceries)

# print(groceries[0])

# print(groceries[0][0])

for collection in groceries:
    # print(collection)
    for food in collection:
        print(food, end=" ")
    print()

    