# # if case
# tag = input("Welcher Tag? ")
# rabatt = 0

# if tag == "Samstag":
#     rabatt = 5
# elif tag == "Sonntag":
#     rabatt = 10
# elif tag == "Montag" or tag == "Dienstag":
#     rabatt = 2
# else:
#     rabatt = 0
# print("Rabatt is heute: ", rabatt)

spam = input("Ein Wert")
match spam:
    case "1":
        print("Eins")
    case "41":
        print("Einundvierzig")
    case _:
        print("Etwas anderes")