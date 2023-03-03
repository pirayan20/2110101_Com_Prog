import math
bd, bm, by, a, b, c = [int(e) for e in input().split()]


def howmanydaysleft(d, m, y):
    y = y-543

    aplus = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    a = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                m = aplus[m-1]
                return(366 - (d + m))
            else:
                m = a[m-1]
                return(365 - (d + m))
        else:
            m = aplus[m-1]
            return(366 - (d + m))
    else:
        m = a[m-1]
        return(365 - (d + m))


def howmanydayspass(d, m, y):
    y = y-543

    aplus = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    a = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                m = aplus[m-1]
                return(d + m)
            else:
                m = a[m-1]
                return(d + m)
        else:
            m = aplus[m-1]
            return(d + m)
    else:
        m = a[m-1]
        return(d + m)


p = howmanydaysleft(bd, bm, by)
q = howmanydayspass(a, b, c)
r = ((c - by)-1)*365

t = p + q + r

physical = math.sin((2*math.pi*t)/23)
emotional = math.sin((2*math.pi*t)/28)
intellectual = math.sin((2*math.pi*t)/33)

print(t, "{:.2f}".format(physical), "{:.2f}".format(emotional), "{:.2f}".format(intellectual))
