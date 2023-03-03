def is_odd(n):
    if n % 2 == 0:
        return False
    else:
        return True


def has_odds(x):
    for i in x:
        if is_odd(i) == True:
            return True
            break
    return False


def all_odds(x):
    for i in x:
        if is_odd(i) == False:
            return False
            break
    return True


def no_odds(x):
    if has_odds(x) == True:
        return False
    else:
        return True


def get_odds(x):
    l = []
    for i in x:
        if is_odd(i) == True:
            l.append(i)
        else:
            pass
    return l


def zip_odds(a, b):
    l1 = get_odds(a)
    l2 = get_odds(b)
    dl = len(l1) - len(l2)
    final = []
    x = 0
    y = 0
    if dl > 0:
        dll = len(l1) - dl
        for i in range(dll*2):
            if i % 2 == 0:
                final.append(l1[x])
                x += 1
            else:
                final.append(l2[y])
                y += 1
        for j in range(dl):
            final.append(l1[dll])
            dll += 1

    elif dl < 0:
        dl = -dl
        dll = len(l2) - dl
        for i in range(dll*2):
            if i % 2 == 0:
                final.append(l1[x])
                x += 1
            else:
                final.append(l2[y])
                y += 1
        for j in range(dl):
            final.append(l2[dll])
            dll += 1

    else:
        for i in range(len(l1)*2):
            if i % 2 == 0:
                final.append(l1[x])
                x += 1
            else:
                final.append(l2[y])
                y += 1

    return final


exec(input().strip())
