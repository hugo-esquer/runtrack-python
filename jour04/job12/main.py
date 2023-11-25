L=[76, 8, 43, 90, 13]

def long(liste):
    count=0
    for i in liste:
        count+=1
    return count

def organiser(liste):   # tri a bulle
    i = long(liste) - 1 #pour parcourir la liste sans dépasser le dernier index
    while i > 0:
        j=0
        while j < i:
            if liste[j+1]<liste[j]: # comparer deux chiffre adjacent si le plus grand est avant :
                stock=liste[j+1]    # stocker le plus petit des deux
                liste[j+1]=liste[j] # faire "avancer" le plus gand
                liste[j]=stock      # faire "reculer" le plus petit
            j+=1
        i-=1        # retier le dernier index des chiffres parcourue, qui est désormais le chiffre le plus grand

print(L)
organiser(L)
print(L)