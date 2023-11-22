def moyenne(a, b, c):
    return (a+b+c)/3

note1 = float(input("Entrer la première note: "))
note2 = float(input("Enter la deuxieme note: "))
note3 = float(input("Entrer la troisième note: "))

moyenne_etudiant = moyenne(note1, note2, note3)

if 20 >= moyenne_etudiant >= 15:
    print("Très bon élève")
elif 14 >= moyenne_etudiant >= 11:
    print("Bon élève")
elif 10 >= moyenne_etudiant >= 8:
    print("Elève moyen")
elif 7 >= moyenne_etudiant >= 0:
    print("Elève devant faire des efforts")
