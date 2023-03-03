x = input()
x = (x[0::].split(" "))
for i in range(0, len(x)):
    x[i] = float(x[i])

max = 0
for k in range(0, len(x)):
    if x[k] > max:
        max = x[k]
    else:
        pass

min = x[0]
for p in range(0, len(x)):
    if x[p] < min:
        min = x[p]
    else:
        pass

print(round((sum(x[0::])-(max + min)) / 2, 2))
