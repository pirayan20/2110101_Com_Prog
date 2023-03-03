x = input()
a = "("
b = ")"
c = "["
d = "]"
y = ""

for i in range(len(x)):
    if x[i] == a:
        y = y+c
        i += 1
    elif x[i] == b:
        y = y+d
        i += 1
    elif x[i] == c:
        y = y+a
        i += 1
    elif x[i] == d:
        y = y+b
        i += 1
    else:
        y = y+x[i]
        i += 1

print(y)
