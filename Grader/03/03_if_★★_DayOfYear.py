d = int(input())
m = int(input())
y = int(input())
y = y-543

aplus = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
a = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            m = aplus[m-1]
            print(d + m)
        else:
            m = a[m-1]
            print(d + m)
    else:
        m = aplus[m-1]
        print(d + m)
else:
    m = a[m-1]
    print(d + m)
