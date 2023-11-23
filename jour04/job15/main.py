def arrondir(num):
    entier = num//1
    decimal = num%1
    if decimal >= 0.5:
        entier+=1
    return entier

def long(liste):
    count=0
    for i in liste:
        count+=1
    return count

def organiser(liste):
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