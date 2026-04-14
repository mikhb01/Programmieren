def spam(name):
    if name == "Schrödinger":
        return "Hi " + name + "!"
    return "Ich kenne dich nicht"

# eingabe = input("Name?")
# print(spam(eingabe))

def zahlenVerdreher(zahl):
    if zahl > 5:
        zahl = zahl - 1
        zahl = zahlenVerdreher(zahl)
        return zahl
    return zahl

print(zahlenVerdreher(10))