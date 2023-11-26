alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",)
def encoder(mot, decalage):
    i=0
    nouveau_mot = ""
    while i < len(mot):
        c = mot[i]
        if c != " ":
            rang = alphabet.index(c)
            rang2 = (rang + decalage)%26
            nouveau_mot += alphabet[rang2]
        elif c == " ":
                nouveau_mot+=c
        i+=1
    return (nouveau_mot)

def decoder(mot, decalage):
    return encoder(mot, -decalage)

mot_code = encoder("codez en python", 4)
print(mot_code)
mot_decode = decoder(mot_code, 4)
print(mot_decode)