n = int(input())
m = n-1
p = 1
for i in range(n):
    if i == 0:
        print(" "*(m)+"*")
        m -= 1
    elif i != n-1:
        print(" "*(m)+"*"+" "*(p)+"*")
        m -= 1
        p += 2
    else:
        print("*"*(2*n-1))
