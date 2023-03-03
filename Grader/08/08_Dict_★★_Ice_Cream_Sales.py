n = int(input())
d = {}
dd = {}
total = 0

for i in range(n):
    s = input().split()
    icname, price = s[0], float(s[1])
    d[icname] = price
    dd[icname] = 0

m = int(input())
for i in range(m):
    income = 0
    p = input().split()
    sell, money = p[0], float(p[1])
    if sell in d:
        income = d[sell] * money
        total += income
        dd[sell] += income
    else:
        pass

l = []
o = max(dd.values())
for e in dd:
    if dd[e] == o:
        l.append(e)
l = sorted(l)
s = ''

if total != 0:
    print("Total ice cream sales:", str(total))
    for i in range(len(l)):
        if i != len(l) - 1:
            s += l[i] + ", "
        else:
            s += l[i]
    print("Top sales:", s)
else:
    print("No ice cream sales")
