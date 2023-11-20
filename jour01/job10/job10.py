montant = 0
rendement = 0
gain = (montant*rendement) / 100
print(gain)
montant += 5_000
rendement += 2
gain = (montant*rendement) / 100
print(gain)
montant = montant - ((montant*10)/100)
rendement -= 1
gain = (montant*rendement) / 100
print(gain)