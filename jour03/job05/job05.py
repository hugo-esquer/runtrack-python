def calcule(num1, operator, num2):
    if operator == "x":
        return num1*num2
    elif operator == "+":
        return num1+num2
    elif operator == "/":
        return num1/num2
    elif operator == "-":
        return num1-num2
    elif operator == "%":
        return num1%num2
    
print(calcule(18, "x", 32))
print(calcule(65, "+", 5))
print(calcule(70, "/", 5))
print(calcule(75, "-", 6))
print(calcule(635, "%", 36))