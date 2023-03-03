n = int(input().strip())
d = {}
k = []

for i in range(n):
    id,allcity = input().split(": ")
    city = allcity.split(', ')
    d[id] = city
    k.append(id)

l = set()
target = input().strip()
for i in d[target]:
    for j in k:
        if i in d[j] and j != target:
            l.add(j)

if len(l) == 0:
    print('Not Found')
else:
    for i in k:
        if i in l:
            print(i)
