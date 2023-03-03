def spiral_square(n):
    idx = int((n-1)/2)
    idy = int((n-1)/2)
    count = 1
    num = 1
    l = []
    for i in range(n):
        if i !=  (n-1)/2:
            l.append([0]*n)
        else:
            s = [0]*n
            s[int((n-1)/2)] = 1
            l.append(s)
    while count <  n:
        if count == n - 1:
            for i in range(3):
                if i == 0:
                    for j in range(count):
                        num += 1
                        idx -= 1
                        l[idy][idx] = num
                elif i == 1:
                    for j in range(count):
                        num += 1
                        idy += 1
                        l[idy][idx] = num
                else:
                    for j in range(count):
                        num += 1
                        idx += 1
                        l[idy][idx] = num
        elif count % 2 == 1:
            for i in range(2):
                if i == 0:
                    for j in range(count):
                        num += 1
                        idx += 1
                        l[idy][idx] = num
                else:
                    for j in range(count):
                        num += 1
                        idy -= 1
                        l[idy][idx] = num
        else:
            for i in range(2):
                if i == 0:
                    for j in range(count):
                        num += 1
                        idx -= 1
                        l[idy][idx] = num
                else:
                    for j in range(count):
                        num += 1
                        idy += 1
                        l[idy][idx] = num
        count += 1

    return l

def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))

exec(input().strip())