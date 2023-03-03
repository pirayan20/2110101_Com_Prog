y = input()
y = y[0::].split(" ")
c = 0

for k in range(len(y)):
    y[k] = int(y[k])


for i in range(len(y)):
    if i == 0:
        pass
    elif i == len(y) - 1:
        pass
    else:
        if y[i] > y[i-1]:
            if y[i] > y[i+1]:
                c += 1
            else:
                pass
        else:
            pass

print(c)
