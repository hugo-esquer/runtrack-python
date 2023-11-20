chaine = input ("Enter un mot ou un phrase: ")
if "e" in chaine and "E" in chaine:
    print ("contient un e et E !")
elif "E" in chaine:
    print("contient un E !")
elif "e" in chaine:
    print("contient un e !")
else:
    print("Ne contient pas de e ni de E")