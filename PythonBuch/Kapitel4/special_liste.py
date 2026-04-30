spam = [7, 'hallo', 3, 42]
def magische42(listen_wert):
    if listen_wert == 42:
        return -1
    if type(listen_wert) == int:
        return listen_wert
    if type(listen_wert) == str:
        return len(listen_wert)
    
spam.sort(key=magische42)
print(spam)

