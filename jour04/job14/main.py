def long(chaine):
    count=0
    for i in chaine:
        count+=1
    return count

def decouper_chaine(chiffre, chaine):
    decoupe = []
    debut = 0
    longueur_chaine = long(chaine)
    i=0

    while i < longueur_chaine:
        if chaine[i] == " " or chaine[i] == ",":
            decoupe += [chaine[debut:i]]
            debut = i+1
        i+=1
    decoupe += [chaine[debut:]]
    nouvelle_phrase =""
    for i in decoupe:
        if long(i) > chiffre:
            nouvelle_phrase += i + " "
    return nouvelle_phrase


print(decouper_chaine(3," la peur est le chemin vers le côtes obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"))