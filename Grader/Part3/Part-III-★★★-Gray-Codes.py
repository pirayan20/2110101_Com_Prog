n = int(input())
k = int(input())
validN = True
validK = True

if type(n) != int or n < 1:
    validN = False

if k < 1:
    validK = False

def gray_code(nbit):
    if nbit == 1:
        return ['0','1']
    else:
        base = gray_code(nbit-1)
        base += base[::-1]
        for i in range(len(base)):
            if i < len(base) /2:
                base[i] = '0'+base[i]
            else:
                base[i] = '1'+base[i]
        return base

if validK and validN:
    out = ''
    for i in range(1,k+1):
        s = ''
        if i != k:
            m = n
        else:
            m = n -1 
        s += str(i)
        while len(s) != m + 1:
            s += '-'
        out += s
    print(out)

    count = (2**n // k)+1
    for i in range(count):
        start = k*i
        print(','.join(gray_code(n)[start:start+k]))


elif validK == False and validN == True:
    print('Invalid k')

elif validK == True and validN == False:
    print('Invalid n')

else:
    print('Invalid n and k')