def paire_impaire(nombre):
    if type(nombre) == int and nombre > 0:
        if nombre % 2 == 0:
            print("le nombre est paire")
        else:
            print("le nombre est impaire")
    else:
        print("Entrer un nombre entier et positif")

paire_impaire(-4)
paire_impaire(4)
paire_impaire(11)
paire_impaire(15)
paire_impaire(76)
paire_impaire(7)
