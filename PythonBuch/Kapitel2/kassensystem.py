# Rabatt 7%
eingabe = "j"
while eingabe == "j":
    preis = input("Gib den Preis ein: ")
    tag = input("Welcher Tag ist heute: ")
    match tag:
        case "Samstag":
            rabatt_in_prozent = 5
        case "Sonntag":
            rabatt_in_prozent = 10
        case "Montag" | "Dienstag":
            rabatt_in_prozent = 2
        case _:
            rabatt_in_prozent = 0
    print("Rabatt ist heute: ", rabatt_in_prozent, "%")

    preis = float(preis)
    rabatt_in_prozent = float(rabatt_in_prozent)
    rabatt_in_euro = preis/100 * rabatt_in_prozent
    neuer_preis = preis - rabatt_in_euro
    print("Preis mit ", rabatt_in_prozent, "% Rabatt ist: ", neuer_preis)

    zahlung = input("Der Kunde zahlt: ")
    zahlung = float(zahlung)
    rueckgeld = zahlung - neuer_preis
    rueckgeld = round(rueckgeld, 2)

    if rueckgeld < 0:
        print("Das gezahlte Geld reicht nicht!")
    else:
        print("Gegeben: ", zahlung, "Preis: ", neuer_preis)
        print("Wechselgeld: ", rueckgeld)

        eingabe = input("Noch einmal? Dann gib 'j' ein!")
print("Das Programm wurde beendet.")

# print(type(preis))
# print(type(zahlung))'


# Kapitel 2 durch