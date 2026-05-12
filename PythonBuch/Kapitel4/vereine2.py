vereine = []

def vereine_sortiert(liste):
    liste.sort()
    zaehler = 0
    for element in liste:
        print(str(zaehler)+ ": " + element)
        zaehler += 1

    

while True:
    neuer_verein = input("Neuer Verein?:")
    if(len(neuer_verein) < 3):
        break

    vereine.append(neuer_verein)
    vereine_sortiert(vereine)
   
    abfrage = input("Willst du einen Verein löschen? (y/n):")
    if abfrage == 'y':

        loeschen = input("Welchen Verein möchtest du löschen?:")
        loeschen = int(loeschen)
    
        if loeschen < len(vereine):
            vereine.pop(loeschen)
        else:
            break

    vereine_sortiert(vereine)