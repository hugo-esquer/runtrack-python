def rectangle(width,height):
    i=0
    if width < 3 or height < 3:
        return print("Erreur: requiers des valeurs supérieur ou égale à 3")
    cotes_h_b = "|"+("-"*(width-2))+"|"
    cotes_g_d = "|"+(" "*(width-2))+"|"
    print(cotes_h_b)
    while i < (height-2):
        print(cotes_g_d)
        i+=1
    print(cotes_h_b)

if __name__ == "__main__":
    rectangle(8, 5)