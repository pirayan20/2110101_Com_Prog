n = int(input())
d = {}
for i in range(n):
    name, nickname = input().split()
    d[name] = nickname

m = int(input())
l = []
for i in range(m):
    s = input()
    if s in d:
        l.append(d[s])
    elif s in d.values():
        for j in d:
            if d[j] == s:
                l.append(j)
                break
    else:
        l.append("Not found")

for i in l:
    print(i)
