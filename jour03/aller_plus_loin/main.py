def inverse(mot):
    mot_inverse=""
    i=1
    while i <= len(mot):
        mot_inverse = mot_inverse + mot[-i]
        i=i+1
    return mot_inverse
    
print(inverse("enutrof"))