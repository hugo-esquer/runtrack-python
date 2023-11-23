L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def multiplication(liste):
    intervalle= []
    for i in liste:
        if 25 < i < 90:
            intervalle.append(i)
    j=1
    for i in intervalle:
        j*= i
    return j
    

print(multiplication(L))