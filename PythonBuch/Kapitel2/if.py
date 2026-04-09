eingabe = input("Gib mir bitte einen Namen: ")

if len(eingabe) != 0:
    if eingabe == "Schrödinger":
        print("Hallo Schrödinger. Schön, dass du hier bist")
    else:
        print("Falscher Benutzer")
else:
    print("Die Eingabe war leer. Bitte starte erneut von vorne")
    