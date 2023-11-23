L=[76, 8, 43, 90, 13]

def minimum(liste):
    num_min=liste[0]
    for i in liste:
        if i < num_min:
            num_min=i
    return num_min


sorted_list=[]
while L:
    sorted_list.append(minimum(L))
    L.remove(minimum(L))

L=sorted_list
print(L)