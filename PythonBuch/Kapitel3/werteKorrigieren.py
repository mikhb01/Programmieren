def werte_korrigieren(zahl):
    if zahl < 0:
        return 0
    if zahl > 10:
        return 10
    return zahl

print(werte_korrigieren(3))