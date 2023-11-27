def triangle(n):
    if n < 2 or type(n) == float :
        return print("Entrer un entier supperieur à 2")
    i=0
    while i < n:
        if i==n-1:
            print((" "*(n-1-i))+"/"+("-"*(i*2))+"\\")
        else:
            print((" "*(n-1-i))+"/"+(" "*(i*2))+"\\")
        i+=1


triangle(int(input("Entrer la hauteur du triangle: ")))