ids = []
grades = []

while True:
    s = input()
    if s != "q":
        s = s[0::].split(" ")
        ids.append(s[0])
        grades.append(s[1])
    else:
        break

uids = input()
uids = uids[0::].split(" ")

before = ["F", "D", "D+", "C", "C+", "B", "B+"]
after = ["D", "D+", "C", "C+", "B", "B+", "A"]

for i in range(len(uids)):
    if uids[i] in ids:
        x = ids.index(uids[i])
        if grades[x] in before:
            y = before.index(grades[x])
            grades[x] = after[y]
        else:
            pass
    else:
        pass
    i += 1

for i in range(len(ids)):
    print(ids[i], grades[i])
