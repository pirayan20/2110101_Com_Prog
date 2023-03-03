
def make_int_list(str):
    x = str.split(" ")
    for i in range(len(x)):
        if x[i] != "":
            x[i] = int(x[i])
        else:
            x = []
    return x


def is_odd(e):
    odd = True
    if int(e) % 2 == 0:
        odd = False
    return odd


def odd_list(alist):
    oddlist = []
    for i in alist:
        if is_odd(i) == True:
            oddlist.append(i)
        else:
            pass
    return oddlist


def sum_square(alist):
    for i in range(len(alist)):
        alist[i] = int(alist[i])**2
    s = sum(alist)
    return s


exec(input().strip())