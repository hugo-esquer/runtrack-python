L=[10,20,30,20,10,50,60,40,80,50,40]
L_unique=[]
for i in L:
    if i not in L_unique:
        L_unique.append(i)

L=L_unique
print(L)