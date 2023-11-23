L=[76, 8, 43, 90, 13]

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

print(L)
organiser(L)
print(L)