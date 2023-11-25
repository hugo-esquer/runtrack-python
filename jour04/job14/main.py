def long(chaine): #fonction pour calculer la longuer d'une chaine
    count=0
    for i in chaine:
        count+=1
    return count

def decouper_chaine(chiffre, chaine):
    decoupe = []                     # liste de mots de la phrase
    debut = 0                        # début du mot
    longueur_chaine = long(chaine)   # taille de la phrase
    nouvelle_phrase =""              # phrase sans les mots trop petit
    i=0

    while i < longueur_chaine:                  # extraire les mots en liste
        if chaine[i] == " " or chaine[i] == ",":# pour chaque espace ou , selectionner le mot
            decoupe += [chaine[debut:i]]
            debut = i+1                         # mettre a jour le début su prochain mot
        i+=1
    decoupe += [chaine[debut:]]                 # ajout du dernier mot de la phrase

    for i in decoupe:                           #retrait des mots inferieur a chiffre
        if long(i) > chiffre:
            nouvelle_phrase += i + " "
    return nouvelle_phrase


print(decouper_chaine(3," La peur est le chemin vers le côtes obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"))