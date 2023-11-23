L=[8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
def add_paire(liste):
    somme=0
    for i in liste:
        if i%2==0:
            somme+= i
    return somme

print(add_paire(L))