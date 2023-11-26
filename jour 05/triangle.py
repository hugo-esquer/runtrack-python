def triangle(n):
    i=0
    while i < n:
        if i==n-1:
            print((" "*(n-1-i))+"/"+("-"*(i*2))+"\\")
        else:
            print((" "*(n-1-i))+"/"+(" "*(i*2))+"\\")
        i+=1


if __name__ == "__main__":
    triangle(8)