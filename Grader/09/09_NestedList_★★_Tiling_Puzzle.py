
def row_number(t, e):
    for i in range(len(t)):
        if e in t[i]:
            return i


def flatten(x):
    l = []
    for i in x:
        if type(i) != list:
            if i != 0:
                l.append(i)
        else:
            l += flatten(i)
    return l


def inversions(lol):
    l = flatten(lol)
    count = 0
    for i in range(len(l)):
        n = i + 1
        while n != len(l):
            if l[i] > l[n]:
                count += 1
            n += 1
    return count


def solvable(t):
    solve = False
    row = row_number(t, 0)
    long = len(t)
    inv = inversions(t)
    if long % 2 != 0 and inv % 2 == 0:
        solve = True
    else:
        if inv % 2 != 0 and row % 2 == 0:
            solve = True
        elif inv % 2 == 0 and row % 2 != 0:
            solve = True
    return solve


exec(input().strip())
