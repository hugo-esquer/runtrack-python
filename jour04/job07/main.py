L=[8, 24, 48, 2, 16]
def multiples(liste):
    count=0
    for i in liste:
        if i%3==0:
            count+=1
    return count
print(multiples(L))