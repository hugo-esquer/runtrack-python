L = [89, 67, 22, 11, 96, 59, 42]

def my_sort(liste):
    
    count = 0                           # definir un compteur d'action
    for i in range(len(liste)):
        
        x = liste[i]                    # mémoriser liste[i] dans une variable

                                        # décaler les éléments liste[0]...liste[i-1] qui sont plus grand que x, en partant de liste[i-1]
        j=i
        while j > 0 and liste[j-1] > x: # parcourir la liste en sens inverse et décaler les chiffre plus grand que x
            liste[j] = liste[j-1]       # décaler [j+1] tant qu'il est plus grand que x
            j = j-1                     # pour continuer à verifier les éléments lors de la boucle suivante
            count+=1                    # compte des actions
        liste[j] = x                    # on "place" l'élément en mémoire dans le "trou" laissé par le décalage

    print(f"Nombre total de coups nécessaire pour trier la liste: {count}")
    print(liste)

my_sort(L)