d = input()
d = d[0::].split()
n = len(d)

for i in range(n):
    d[i] = int(d[i])

i = -1
j = 0
p = d[n-1]

while j < n-1:
    if d[j] <= p:
        i += 1
        d[i], d[j] = d[j], d[i]
    else:
        pass
    j += 1

d[i+1], d[n-1] = d[n-1], d[i+1]
print(d)
