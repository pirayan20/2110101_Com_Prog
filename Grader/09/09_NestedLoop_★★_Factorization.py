def factor(n):
    l = []
    for i in range(2, n+1):
        if n == 1:
            break
        else:
            c = 0
            while n/i >= 1:
                if n % i != 0:
                    break
                else:
                    c += 1
                    n /= i
            if c != 0:
                l.append([i, c])
    return l


exec(input().strip())
