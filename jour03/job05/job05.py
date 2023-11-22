def calcule(num1, operateur, num2):
    if operateur == "x":
        return num1*num2
    elif operateur == "+":
        return num1+num2
    elif operateur == "/":
        return num1/num2
    elif operateur == "-":
        return num1-num2
    elif operateur == "%":
        return num1%num2
    else:
        return "Entrer un opérateur valide"
    
print(calcule(18, "x", 32))
print(calcule(65, "+", 5))
print(calcule(70, "/", 5))
print(calcule(75, "-", 6))
print(calcule(635, "%", 36))
print(calcule(56, "v", 67))