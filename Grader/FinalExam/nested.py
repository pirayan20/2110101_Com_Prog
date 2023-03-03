import numpy as np

def pattern1(N):
    num = 1
    l = []
    for i in range(N):
        c = []
        for j in range(i + 1):
            c.append(num)
            num += 1
        while len(c) != N :
            c.append(0)
        l.append(c)
    a = np.array(l)
    a = np.flipud(a)
    ans = []
    for i in a:
        ans.append(list(i))
    return ans

def pattern2(N):
    num = 1
    l = []
    for i in range(N):
        j = 0
        c = []
        c += [0]*i
        while len(c) != N:
            c.append(num+j)
            j += 1
        l.append(c)
        num += N - i
    x = np.array(l)
    for i in range(3):
        x = np.rot90(x)
    x = np.flipud(x)
    ans = []
    for i in x:
        ans.append(list(i))
    return ans

print(pattern2(5))