spam = [42, 'hallo', 13, True]
print(spam)
print(spam[0])
print(spam[1])
print(spam[-1])
print(spam[-3])

spam[1] = "Moin Schrödinger"
print(spam)

print(len(spam))

zwischenergebnis = spam[2]
ergebnis = spam[0] * zwischenergebnis
print(ergebnis)


spam = [1, 2, 3, 4, 5, 6, 7, 8, 9]
teil_liste = spam[1:5]
print(teil_liste)
print(spam[-5:-2])