import math
n = input().split(',')
x = n[0] + "." + n[1]
x = float(x)
upper = int(x*(10**len(n[1])))
lower = int(10**len(n[1]))

bon = int(n[2])
lhang = (10**len(n[2])-1)*(10**(len(n[1])))

a = upper*lhang + bon*lower
b = lower*lhang

hrm = math.gcd(a, b)

p = int(a//hrm)
q = int(b//hrm)

print(p, "/", q)
