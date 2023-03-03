def in_all(malls):
    all = []
    for key in malls:
        all.append(set(malls[key]))
    for i in range(len(all)):
        if i == 0:
            inter = all[i]
        else:
            inter = inter.intersection(all[i])

    return sorted(list(inter))

def only_one(malls):
    ans = []
    all = []
    for key in malls:  
        all.append(set(malls[key]))
    for i in range(len(malls)):
        if i == 0:
            un = all[i]
        else:
            un = un.union(all[i])
    un = list(un)
    for i in un:
        count = 0
        for j in all:
            if i in list(j):
                count += 1
        if count == 1:
            ans.append(i)
    return sorted(ans)


exec(input().strip())