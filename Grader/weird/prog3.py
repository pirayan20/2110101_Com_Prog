
def moving_average(x, n):
    l = []
    i = 0
    x = x[::-1]
    while n > 0:
        while i+n <= len(x):
            avg = 0
            for e in range(n):
                avg += x[i+e]
            avg /= n
            l.append(avg)
            i += 1
        n -= 1
    return l[::-1]


print(moving_average([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
