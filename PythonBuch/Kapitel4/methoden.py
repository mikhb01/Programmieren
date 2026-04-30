#extend
spam = [1, 2, 7]
egg = ["Hi", 41, 1]
spam.extend(egg)
spam.extend([12, 3])
print(spam)

#insert
spam = ["Hier", "Da", "Dort"]
spam.insert(0, "Erster")
spam.insert(2, "Auch dabei")
print(spam)

spam = ["Hier", "Da", "Dort"]
eggs = ["Links", "Rechts"]
spam.insert(1, eggs)
print(spam)

#reverse
meine_liste = [1, 2, 3]
meine_liste.reverse()
print(meine_liste)

#sort
spam = [42, 1, 90, 17]
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

#pop
meine_liste = [1, 2, 3, 4, 5, 6]
meine_liste.pop()
print(meine_liste)
meine_liste.pop(1)
print(meine_liste)
entfernt = meine_liste.pop()
print(entfernt)
print(meine_liste)

#index
spam = ["Bert", "Klaus", "John", "Pjotr"]
print(spam.index("John"))

#remove
spam = ["Hier", "Da", "Dort", "Da"]
print(spam)
spam.remove("Da")
print(spam)
spam.remove("Da")
print(spam)

#count
spam = ["Hier", "Da", "Dort", "Da"]
print(spam.count("Da"))
print(spam.count("Irgendwo"))

#in
spam = ["Links", "Rechts", "Oben"]
print("Unten" in spam)
print("Oben" in spam)

#in mit for 
spam = ["Links", "Rechts", "Oben"]
if "Unten" in spam:
    spam.remove("Unten")
if "Oben" in spam:
    spam.remove("Oben")
print(spam)