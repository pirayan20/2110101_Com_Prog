l = []
while True:
    s = input()
    if s != "end":
        l.append(s)
    else:
        break

a = ["a", "b", "c", "d", "e", "f", 'g', 'h', 'i', 'j', 'k', 'l', 'm']
b = ["n", 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(l)):
    s = ''
    for j in range(len(l[i])):
        if l[i][j] in a:
            m = a.index(l[i][j])
            s += b[m]
        elif l[i][j] in b:
            m = b.index(l[i][j])
            s += a[m]
        elif l[i][j].lower() in a:
            m = a.index(l[i][j].lower())
            s += b[m].upper()
        elif l[i][j].lower() in b:
            m = b.index(l[i][j].lower())
            s += a[m].upper()
        else:
            s += l[i][j]

    print(s)
