def first_fit(L, e):
    c = 0
    for i in L:
        if sum(i) + e <= 100:
            i.append(e)
            break
        else:
            c += 1
    if c == len(L):
        L.append([e])
    return L
    
    
def best_fit(L, e):
    c = 0
    k = []
    for i in L:
        k.append(100 -(sum(i) +e))
    sort_k = sorted(k)
    for i in sort_k:
        if i >= 0:
            L[k.index(i)].append(e)
            break
        else:
            c += 1
    if c == len(L):
        L.append([e])


def partition_FF(D):
    l = []
    l.append([D[0]])
    for i in range(1,len(D)):
        first_fit(l,D[i])
    return l
    

def partition_BF(D):
    l = []
    l.append([D[0]])
    for i in range(1,len(D)):
        best_fit(l,D[i])
    return l


exec(input().strip())        

