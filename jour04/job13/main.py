L=[10,20,30,20,10,50,60,40,80,50,40]
def long(liste):
    count=0
    for i in liste:
        count+=1
    return count

def doublons(liste):
    i=0
    while i < long(liste):
        if liste[i] in liste[i+1:]:
            liste[i:i+1]=[]
        i+=1

print(L)
doublons(L)
print(L)