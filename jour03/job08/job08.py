def de_saison(type, saison):
    if type == "fruits":
        if saison == "hiver":
            print("orange, mandarine et kiwi")
        elif saison == "ete":
            print("Poire, fraise, cassis")
    elif type == "legume":
        if saison == "hiver":
            print("carotte, topinambour, endive")
        elif saison == "été":
            print("artichaut, aubergine, navet")


de_saison("fruits", "ete")
de_saison("legume", "hiver")