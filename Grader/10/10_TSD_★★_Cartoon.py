d = {}
l = []
while True:
    s = input().strip()
    if s != "q":
        name, animal = s.split(', ')
        if animal not in d:
            d[animal] = []
            l.append(animal)
        d[animal].append(name)
    else:
        break

for i in l:
    print(i+": "+', '.join(d[i]))
