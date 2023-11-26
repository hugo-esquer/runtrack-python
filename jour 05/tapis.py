def tapis(n):
    cadre = "+"+"-"*(n+1)+"+"
    i=0
    print(cadre)
    while i < (n+1):
        print("|"+"#"*(n-i)+" "+"#"*(1*i)+"|")
        i+=1
    print(cadre)

tapis(10)
