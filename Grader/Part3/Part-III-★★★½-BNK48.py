globalscore = {}
globalvote = {}
globalkami = {}

def reverse(d):
    m = {}
    for i in d:
        m[d[i]] = i
    return m

while True:
    s = input().strip()
    if s not in "123":
        ota, member, point = s.split()
        if member not in globalscore:
            globalscore[member] = 0
        globalscore[member] += int(point)
        if member not in globalvote:
            globalvote[member] = set()
        globalvote[member].add(ota)
        if ota not in globalkami:
            globalkami[ota] = {}
        if member not in globalkami[ota]:
            globalkami[ota][member] = 0
        globalkami[ota][member] += int(point)

    elif s == "1":
        l = []
        k = sorted(list(globalscore.values()))[::-1]
        for i in range(3):
            for member in globalscore:
                if k[i] == globalscore[member]:
                    l.append(member)
                    break
        print(", ".join(l))
        break    

    elif s == "2":
        l = []
        k = []
        for member in globalvote:
            l.append([len(globalvote[member]),member])
        l = sorted(l)[::-1]
        for i in range(3):
            k.append(l[i][1])
        print(", ".join(k))
        break

    elif s == "3":
        s = []
        kamimem = {}
        for ota in globalkami:
            maxi = max(list(globalkami[ota].values()))
            l = []
            for i in globalkami[ota]:
                if globalkami[ota][i] == maxi:
                    l.append(i)
                if i not in kamimem:
                    kamimem[i] = 0
            if len(l) > 1:
                l = sorted(l)
            kamimem[l[0]] += 1
        k = sorted(list(kamimem.values()))[::-1]
        for i in range(3):
            for member in kamimem:
                if kamimem[member] == k[i]:
                    s.append(member)
                    break
        print(', '.join(s))
        break

