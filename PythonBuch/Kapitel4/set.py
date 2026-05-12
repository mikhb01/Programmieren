spam = { 42, 13, 7}
neuer_wert = "Hallo"
if neuer_wert in spam:
    print("Dieser Wert ist bereits vorhanden")
else:
    spam.add(neuer_wert)
print(spam)