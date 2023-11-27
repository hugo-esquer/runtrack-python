def metre(nbr_marche, taille):
    nbr_marche_semaines = (float(nbr_marche)*5*2)*7
    cm_parcouru = nbr_marche_semaines*float(taille)
    metre_parcouru = cm_parcouru/100
    return f"Pour {nbr_marche} marches de {taille} cm, le gardien parcourt {metre_parcouru} m par semaine."

print(metre(20, 17))