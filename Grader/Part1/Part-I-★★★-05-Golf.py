allstroke = []
allpar = []
handicap = []
for i in range(9):
    s = input().split(" ")
    allpar.append(int(s[0]))
    allstroke.append(int(s[1]))
    if s[2] == "1":
        par = int(s[0]) + 2
        s[1] = int(s[1])
        if par > s[1]:
            handicap.append(s[1])
        else:
            handicap.append(par)

allpar = sum(allpar)
allstroke = sum(allstroke)
handicap = sum(handicap)

val = handicap*1.5 - allpar
val *= 0.8
val = val//1

result = allstroke - val

print(allstroke)
print(int(val))
print(int(result))
