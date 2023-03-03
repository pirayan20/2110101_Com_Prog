a = float(input())
L = 0
U = a
x = (L + U) / 2
while abs(a - 10**x) > 10**-10*max(a, 10**x):
    if 10**x > a:
        L, U = L, x
    else:
        L, U = x, U
    x = (L + U) / 2

print(round(x, 6))
