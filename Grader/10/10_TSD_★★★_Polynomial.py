def store(p):
    d = {}
    for i in p:
        d[i[1]] = i[0]
    return d


def add_poly(p1,p2):
    l = []
    d = {}
    for i in p1:
        d[i[1]] = i[0]
    for i in p2:
        if i[1] not in d:
            d[i[1]] = i[0]
        else:
            d[i[1]] += i[0]
    
    for i in d:
        if d[i] != 0:
            l.append([i,d[i]])
    ans = []
    l = sorted(l)[::-1]
    for i in l:
        ans.append((i[1],i[0]))
    return ans


def mult_poly(p1,p2):
    l = []
    d = {}
    p1 = store(p1)
    p2 = store(p2)
    for i in p1:
        for j in p2:
            if i+j not in d:
                d[i+j] = 0
            d[i+j] += p1[i]*p2[j]

    for i in d:
        if d[i] != 0:
            l.append([i,d[i]])
    ans = []
    l = sorted(l)[::-1]
    for i in l:
        ans.append((i[1],i[0]))
    return ans

for i in range(3):
    exec(input().strip())
