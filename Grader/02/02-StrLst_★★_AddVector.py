x = input()
y = input()
x = (x[1:-1].split(","))
y = (y[1:-1].split(","))

for i in range(len(x)):
    x[i] = float(x[i])

for i in range(len(y)):
    y[i] = float(y[i])

z = [0]*3
for i in range(3):
    z[i] = x[i] + y[i]

print(x, "+", y, "=", z)
