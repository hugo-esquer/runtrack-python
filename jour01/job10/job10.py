montant = 1500
rendement = 15
gain = (montant*rendement) / 100
print(f"Les gains sont de {gain}")
montant += 5_000 + gain
rendement += 2
gain = (montant*rendement) / 100
print(f"Les nouveaux gains sont de {gain}")
montant = montant + gain
montant = montant - ((montant*10)/100)
rendement -= 1
gain = (montant*rendement) / 100
print(f"Le montant des gain finaux est de {gain}")