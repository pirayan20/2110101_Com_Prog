d, m, y = [int(e) for e in input().split()]
y = y - 543
n = 31
if m in [4, 6, 9, 11]:
    n = 30
else:
    pass

if m != 2:
    pass
else:
    n = 28
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        n = 29
    else:
        pass

d += 15

if d > n:
    d = d - n
    m = m + 1
else:
    pass

if m > 12:
    m = m - 12
    y = y + 1
else:
    pass

y = y + 543
print(str(d)+"/"+str(m)+"/"+str(y))
