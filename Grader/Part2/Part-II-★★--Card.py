def compare(x, y):
    alpha = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
    kind = ["C", "D", "H", "S"]
    if x[0] != y[0]:
        result = alpha.index(x[0]) - alpha.index(y[0])
        if result > 0:
            return "+"+str(result)
        else:
            return str(result)

    elif x[1] != y[1]:
        result = kind.index(x[1]) - kind.index(y[1])
        if result > 0:
            return "+"+str(result)
        else:
            return str(result)
    else:
        return "0"

        
x = input()
n = 0
dn = 2
l = []

for i in range(int(len(x)/2)):
    l.append(x[n:dn])
    n += 2
    dn += 2

s = ''
for j in range(len(l)-1):
    s += compare(l[j], l[j+1])

print(s)
