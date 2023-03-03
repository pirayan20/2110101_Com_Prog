x = input()
y = input()
notallowed = '"', "(", ")", ",", ".", "'"
for i in notallowed:
    y = y.replace(i, " ")

y = y[0::].split(" ")

c = 0
for k in range(len(y)):
    if y[k] == x:
        c += 1

print(c)
