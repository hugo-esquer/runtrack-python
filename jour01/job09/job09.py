nom = "Paquet de Cigarettes"
prix = 11.50
stock = 20
print(nom + ", prix: " + str(prix) + ", en stock: " + str(stock))
stock += 10
qte = input("Quelle quantité voulez-vous acheter ? ")
qte = float(qte)
stock = stock - qte
prix = prix + ((prix * 10) / 100)
print(nom + ", prix: " + str(prix) + ", en stock: " + str(stock))