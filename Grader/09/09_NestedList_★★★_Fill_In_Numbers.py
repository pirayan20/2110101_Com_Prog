def pattern1(nrows, ncols):
    n = 1
    l = []
    for i in range(nrows):
        c = []
        for j in range(ncols):
            c.append(n+j)
        l.append(c)
        n += ncols
    return l


def pattern2(nrows, ncols):
    l = []
    for i in range(nrows):
        k = i+1-nrows
        c = []
        for j in range(ncols):
            k += nrows
            c.append(k)
        l.append(c)
    return l


def pattern3(n):
    num = 1
    l = []
    for i in range(n):
        j = 0
        c = []
        c += [0]*i
        while len(c) != n:
            c.append(num+j)
            j += 1
        l.append(c)
        num += n - i
    return l


def pattern4(n):
    idx = 1
    num = 0
    l = []
    for i in range(n):
        k = i + 2
        num = idx
        c = []
        c += [0]*i
        while len(c) != n:
            c.append(num)
            num += k
            k += 1
        l.append(c)
        idx += i + 1
    return l


def pattern5(n):
    l = []
    for i in range(n):
        num = i + 1
        c = []
        c += [0]*i
        for j in range(n - len(c)): 
            c.append(num)
            num += n-j
        l.append(c)
    return l    


def pattern6(n): # if n = 5
    num = 1
    l = []
    for idx in range(n):
        if idx == 0:
            for i in range(n):
                c = [0]*n
                c[i] = num
                num += 1
                l.append(c)

        elif idx %2 != 0:
            seq = n -idx #4
            for i in range(seq):
                l[seq-(i+1)][n-(i+1)] = num
                num += 1

        else:
            seq = n -idx #3
            for i in range(seq):
                l[i][i+idx] = num
                num += 1
        
    return l


# exec(input().strip())
a = pattern5(10)
for i in a:
    print(i)
