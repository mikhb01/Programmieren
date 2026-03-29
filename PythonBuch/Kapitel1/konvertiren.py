eingabe = 3
if type(eingabe) == str:
    print("Ein String!")

spam = "10" * 42
print(type(spam))
spam = int("42") > 30
print(type(spam))
egg = 12.0 * 3
print(type(egg))
ergebnis = spam * egg
print(type(ergebnis))