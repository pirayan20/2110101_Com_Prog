def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    return m


def mult_c(c, A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] *= c
    return A


def mult(A, B):
    c = []
    for i in range(len(A)):
        l = []
        for j in range(len(B[0])):
            n = 0
            for k in range(len(A[0])):
                n += A[i][k]*B[k][j]
            l.append(n)
        c.append(l)

    return c


exec(input().strip())
