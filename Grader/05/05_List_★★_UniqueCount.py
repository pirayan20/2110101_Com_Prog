x = input()
x = x[0::].split(" ")

for i in range(len(x)):
    x[i] = int(x[i])

x = sorted(x)

c = 0
y = []
i = 1

while i <= len(x)-1:
    if x[i] != x[i-1]:
        if x[i] == x[len(x)-1]:
            y.append(x[i-1])
            y.append(x[i])
        else:
            y.append(x[i-1])
        c += 1
        i += 1
    else:

        i += 1

print(c+1)
if len(y) < 10:
    print(y)
else:
    print(y[0:10])
