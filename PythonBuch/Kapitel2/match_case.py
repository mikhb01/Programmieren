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


tag = input("Welcher Tag?: ")
stunde = input("Stunde?: ")

match [tag, stunde]:
    case ['Montag', '12']:
        print("Montagmittagsrabatt - 7%")
        super_rabatt = 7
    case ["Mittwoch", "14"]:
        print("Mittwochnachmittagsrabatt - 14%")
        super_rabatt = 14
    case _:
        print("Kein Rabatt")
        super_rabatt = 0
print("Superrabatt: ", super_rabatt)