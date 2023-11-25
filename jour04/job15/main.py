def arrondir(num):      # fonction qui arrondie les nombre
    entier = num//1     # récupérer l'entier
    decimal = num%1     # récupérer le reste
    if decimal >= 0.5:  # arrondir au supérieur 
        entier+=1
    return entier

def long(liste):        # fonction qui retourne la longueur
    count=0
    for i in liste:
        count+=1
    return count

def organiser(liste):   # tri a bulle
    i = long(liste) - 1
    while i > 0:
        j=0
        while j < i:
            if liste[j+1]<liste[j]:
                stock=liste[j+1]
                liste[j+1]=liste[j]
                liste[j]=stock
            j+=1
        i-=1

L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

L_arrondie = []
for i in L:
    L_arrondie +=[arrondir(i)]

organiser(L_arrondie)
print(L_arrondie)