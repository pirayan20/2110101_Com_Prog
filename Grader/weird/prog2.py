c1 = (input().split())
c2 = (input().split())
d = {}
d["A"] = "14"
d["K"] = "13"
d["Q"] = "12"
d["J"] = "11"

for i in range(len(c1)):
    if c1[i] in d:
        c1[i] = d[c1[i]]
for i in range(len(c2)):
    if c2[i] in d:
        c2[i] = d[c2[i]]

for i in range(len(c1)):
    c1[i] = int(c1[i])
for i in range(len(c2)):
    c2[i] = int(c2[i])

c1 = sorted(c1)
c2 = sorted(c2)

if c1[2] == c2[2]:
    if c1[1] == c2[1]:
        if c1[0] == c2[0]:
            print("Draw")
        elif c1[0] > c2[0]:
            print("A win")
        else:
            print("B win")
    elif c1[1] > c2[1]:
        print("A win")
    else:
        print("B win")
elif c1[2] > c2[2]:
    print("A win")
else:
    print("B win")
