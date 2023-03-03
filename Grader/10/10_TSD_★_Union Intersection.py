n = int(input().strip())
l = []
for i in range(n):
    s = set([int(e) for e in input().split()])
    l.append(s)

u = set()
for i in range(len(l)):
    u = u.union(l[i])

inter = set()
for i in range(len(l)):
    if i == 0:
        inter = l[i]
    else:
        inter = inter.intersection(l[i])

print(len(u))
print(len(inter))
