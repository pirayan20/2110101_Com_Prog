import math
n = int(input())
x = []
y = []
alldist = []
seq = []
for i in range(n):
    s = input().split(" ")
    x.append(float(s[0]))
    y.append(float(s[1]))
    seq.append(i)

for i in range(n):
    dist = math.sqrt((x[i])**2 + y[i]**2)
    alldist.append(dist)

sortdist = sorted(alldist)

k = alldist.index(sortdist[2])

print("#"+str(k+1)+":", "("+str(x[k])+",", str(y[k])+")")
