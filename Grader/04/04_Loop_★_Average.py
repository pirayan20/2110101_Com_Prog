lines = []
while True:
    s = input()
    if s != "q":
        lines.append(s)
    else:
        break

c = 0
for i in range(len(lines)):
    c += float(lines[i])

if c == 0:
    print("No Data")
else:
    print(round(c/len(lines), 2))
