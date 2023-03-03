n = int(input())
x = []
y = ""
z = ''
for i in range(n):
    s = input().split(" ")
    x.append(s)

how = input()

for i in range(len(x)):
    if i % 2 == 0:
        p = x[i]
        y = y + " " + str(p[0]) + " "
        z = z + " " + str(p[1]) + " "
    else:
        p = x[i]
        y = y + " " + str(p[1]) + " "
        z = z + " " + str(p[0]) + " "

y = y[0::].split()
z = z[0::].split()

for i in range(len(y)):
    y[i] = int(y[i])

for i in range(len(z)):
    z[i] = int(z[i])

if how == "Zag-Zig":
    print(min(z), max(y))

else:
    print(min(y), max(z))
