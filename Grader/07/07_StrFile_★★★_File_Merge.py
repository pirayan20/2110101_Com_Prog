def read_next(f):
    while True:
        t = f.readline()
        if len(t) == 0:
            break
        x = t.strip().split()
        if len(x) == 2:
            return x[0], x[1]
    return "", ""


name1, name2 = input().strip().split()
func1 = open(name1)
func2 = open(name2)

id1, g1 = read_next(func1)
id2, g2 = read_next(func2)

while id1 != "" and id2 != "":
    if int(id1[-2:]) == int(id2[-2:]):
        if int(id1[:2]) == int(id2[:2]):
            if int(id1[3:8]) < int(id2[3:8]):
                print(id1, g1)
                id1, g1 = read_next(func1)
            else:
                print(id2, g2)
                id2, g2 = read_next(func2)

        elif int(id1[:2]) < int(id2[:2]):
            print(id1, g1)
            id1, g1 = read_next(func1)

        else:
            print(id2, g2)
            id2, g2 = read_next(func2)

    elif int(id1[-2:]) < int(id2[-2:]):
        print(id1, g1)
        id1, g1 = read_next(func1)

    else:
        print(id2, g2)
        id2, g2 = read_next(func2)

while id1 == "" and id2 != "":
    print(id2, g2)
    id2, g2 = read_next(func2)

while id2 == "" and id1 != "":
    print(id1, g1)
    id1, g1 = read_next(func1)

func1.close()
func2.close()
