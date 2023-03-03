nm = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def days_in_feb(y):
    y1 = y-543
    days_in_feb1 = 28
    if y1 % 400 == 0 or y1 % 100 != 0 and y1 % 4 == 0:
        days_in_feb1 = 29
    return days_in_feb1


def dayspass(d, m, y):
    aplus = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    a = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    if days_in_feb(y) == 29:
        return d + aplus[m-1]
    else:
        return d + a[m-1]


l = []
errordict = []
normal = []

while True:
    invalid = False
    string = ''
    s = input().strip()
    if s != "END":
        inf = s.split()
        id, command, d, m, y = inf[0], inf[1], int(inf[2]), int(inf[3]), int(inf[4])

        if y < 2558:
            invalid = True
            string += "Error: "+s+" --> Invalid year"
            l.append(string)
            errordict.append(string)

        elif not (1 <= m <= 12):
            invalid = True
            string += "Error: "+s+" --> Invalid month"
            errordict.append(string)

        if invalid == False:
            nm[1] = days_in_feb(y)
            if not (0 < d <= nm[m-1]):
                invalid = True
                string += "Error: "+s+" --> Invalid date"
                errordict.append(string)

        if invalid == False:
            if command not in "EQNF":
                invalid = True
                string += "Error: "+s+" --> Invalid delivery type"
                errordict.append(string)

        if invalid == False:
            nm[1] = days_in_feb(y)
            if command == "E":
                d += 1
            elif command == "Q":
                d += 3
            elif command == "N":
                d += 7
            elif command == "F":
                d += 14

            if d > nm[m-1]:
                d -= nm[m-1]
                m += 1
                if m > 12:
                    m -= 12
                    y += 1
            string = id + ": delivered on " + str(d) + "/" + str(m) + "/" + str(y)
            normal.append([y, dayspass(d, m, y), string])

    else:
        break

normal.sort()

for i in errordict:
    print(i)
for i in range(len(normal)):
    print(normal[i][2])
