vereine = [
    "1. FC Dinkel", 
    "SpVgg Hornberg", 
    "1. FC Übern Berg"
    ]

vereine.append("2. FC Für die Katz")
print(vereine)

spieler = [
    "Hansi",
    "Bernd", 
    "Diego", 
    "Basti",
    "Riccardo",
    "John"
]

for personen in spieler:
    print(personen)

# #einfache Version
# for der_index in range(0, 6, 2):
#     print(spieler[der_index], spieler[der_index+1])

#bessere Version
for i in range(0, len(spieler), 2):
    print(spieler[i:i+2])

tore = [5, 7, 1, 3, 9, 11, 0]
versuche = len(tore)
bestes_ergebnis = max(tore)
schlechtestes_ergebnis = min(tore)
print(versuche, bestes_ergebnis, schlechtestes_ergebnis)

