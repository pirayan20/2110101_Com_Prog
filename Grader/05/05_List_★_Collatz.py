n = int(input())
all = []
s = ""
while n != 1:
    all.append(int(n))
    if n % 2 == 0:
        n = n/2
    else:
        n = 3*n + 1
all.append(1)

if len(all) > 15:
    all = all[len(all)-15::]
    for i in range(len(all)):
        if i != len(all) - 1:
            s += str(all[i]) + "->"
        else:
            s += str(all[i])
else:
    for i in range(len(all)):
        if i != len(all)-1:
            s += str(all[i]) + "->"
        else:
            s += str(all[i])

print(s)
