L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
def maximum(liste):
    num_max=liste[0]
    for i in liste:
        if i > num_max:
            num_max=i
    return f"la valeur max est : {num_max}"

def minimum(liste):
    num_min=liste[0]
    for i in liste:
        if i < num_min:
            num_min=i
    return f"la valeur min est : {num_min}"

print(maximum(L))
print(minimum(L))