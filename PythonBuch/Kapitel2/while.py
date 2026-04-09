# spam = 10
# eggs = 2
# while spam > eggs:
#     print(eggs)
#     eggs = eggs + 1


# eingabe = "j"
# while eingabe == "j":
#     print("Hallo Schrödinger, ich bin in der Schleife")
#     eingabe = input("Noch einmal? Dann gib 'j' ein!")
# print("Oh, großer Schrödinger: Die Schleife wurde verlassen")

# spam = int(input("Wert?"))
# while spam < 42:
#     print(spam, "ist zu klein")
#     spam = int(input("Wert?"))
# print(spam, "ist groß genug!")

while (spam := int(input("Wert? "))) < 42:
    print(spam, " ist zu klein!")
print(spam, "ist groß genug!")