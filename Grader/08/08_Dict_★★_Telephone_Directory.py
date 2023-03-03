n = int(input())
nametotel = {}
teltoname = {}
for i in range(n):
    s = input().split()
    name = s[0]+' '+s[1]
    telephone = s[2]
    nametotel[name] = telephone
    teltoname[telephone] = name

m = int(input())
l = []
for j in range(m):
    p = input()
    if p in nametotel:
        l.append(p+" --> "+nametotel[p])
    elif p in teltoname:
        l.append(p+" --> "+teltoname[p])
    else:
        l.append(p+" --> Not found")

for i in l:
    print(i)
