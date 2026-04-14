def kassenvorgang():
    preis = input("Gib den Preis ein: ")
    preis = float(preis)
    zahlung = input("Der Kunde zahlt: ")
    zahlung = float(zahlung)
    rueckgeld = zahlung - preis
    print("Gegeben: ", zahlung, "Preis: ", preis)
    print("Wechselgeld: ", rueckgeld)
    return preis

eingabe = "j"
umsatz = 0
while eingabe == "j":
    umsatz = umsatz + kassenvorgang()
    eingabe = input("Noch einmal? Dann gib 'j' ein! ")
print("Der Umsatz beträgt: ", umsatz)
print("Das Programm wurde beendet")

