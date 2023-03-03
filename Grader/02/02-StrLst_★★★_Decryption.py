num = (input())
a = int(num[3]+num[10]+num[17]+num[24]+num[31])
b = int(num[7]+num[12]+num[17]+num[22]+num[27])
c = str(a + b + 10000)
d = c[-2:-5:-1]
d = d[::-1]

x = int(d[0])
y = int(d[1])
z = int(d[2])

p = str(x)+str(y)+str(z)

t = str(x+y+z)

q = int(t[-1])
q += 1

M = ["A","B","C","D","E","F","G","H","I","J"]

q -=1 
n = M[q]

print(p+n)










