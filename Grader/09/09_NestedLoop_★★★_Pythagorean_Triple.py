def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a


def is_coprime(a, b, c):
    k = gcd(b,c)
    if gcd(a,k) == 1:
        return True
    else:
        return False


def primitive_Pythagorean_triples(max_len):
    triple = []
    for i in range(1,max_len+1):
        for j in range(i+1,max_len+1):
            for k in range(j+1,max_len+1):
                if is_coprime(i,j,k) == True and i**2 + j**2 == k**2:
                    triple.append([k,i,j])
                    break
                
    triple.sort()
    for i in range(len(triple)):
        c,a,b = triple[i][0],triple[i][1],triple[i][2]
        triple[i] = [a,b,c]

    return triple
    

exec(input().strip())