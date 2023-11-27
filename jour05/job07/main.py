L = [38, 43, 67, 82, 98, 24, 54, 63, 78]


def arrondi(liste):
    nouvelle_liste = []
    for note in liste: 
        if note > 40:
            prochain_multiple = (note//5+1)*5
            if (prochain_multiple-note) < 3:
                note=prochain_multiple
                nouvelle_liste += [note]
            else:
                nouvelle_liste+=[note]
        else:
            nouvelle_liste +=[note]
    return nouvelle_liste

print(L)
print(arrondi(L))