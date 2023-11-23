def inversion(liste):
    premier=liste[0]
    dernier=liste[-1]
    liste[0]=dernier
    liste[-1]=premier

L=[1, 2, 3, 4, 5]
print(L)
inversion(L)
print(L)