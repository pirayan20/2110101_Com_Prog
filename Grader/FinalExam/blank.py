# no.1/11
# var = 0
# j = 2
# k = 1
# while j <= 5:
#     while k <= 6:
#         var += (k**j)*((j-k)**k)
#         k += 1
#     j += 1
# print(var)

# no.2/11
# def f(d):
#     x = {}
#     for k in d:
#         for e in d[k]:
#             x[e] = k
#     return x

# d = {'pie':{'1234','2345'},'santa':{'5455'}}
# print(f(d))

# no.3/11
# def f1(x): 
#     c = []
#     for e in x:
#         if e.lower() not in 'aeiou':
#             c += [e]
#     return c

# def f2(x):
#     return [e for e in x if e.lower() not in 'aeiou']

# print(f2('pijan'))

# no.4/11
# import numpy as np
# def f1(x): # x เป็น 1-D numpy array of floats
#     n = len(x)
#     p = np.ndarray((n,n))
#     for r in range(n):
#         for c in range(n):
#             p[r,c] = x[r]+x[c]
#     return p

# def f2(x):
#     a = x.reshape(x.size,1)
#     return x+a

# x = np.array([1.0,2.0,3.0])
# print(f2(x))

# no.5/11
# def f(R, C):
#     for i in range(R):
#         out = ''
#         for j in range(C):
#             n = (j+1)+(i*R)
#             out += ('   ' + str(n))[-4:]
#         print(out)

# f(5, 10)

# no.6/11 --> ไม่ชัวว่า input หน้าตาเป็นไง
# def f(d):
#     x = {}
#     for e in list(d.values()):
#         x[e] = []
#     for k in d:
#         for e in d[k]:
#             x[e] += [k]
#     return x

# d = {'1234':'pie','2345':'pie','0987':'santa'}
# print(f(d))

# no.7/11
# จำนวนบรรทัดที่มีอยู่ในไฟล์

# no.8/11
# class A: 
#     def __init__(self, a, b):
#         self.s = [a,b]
#     def __str__(self):
#         return ':'.join([(' '+str(e))[-2:] for e in self.s])
#     def f(self):
#         return A(-self.s[0],-self.s[1])

# a1 = A(9,1)
# a2 = a1.f()
# a3 = a2.f()
# print(a1)
# print(a2)
# print(a3)

# no.9/11
# import numpy as np
# def f1(z, c): 
#     # z เป็น 1-D numpy array of ints, c เป็น int
#     n = z[0]
#     for e in z[1:]:
#         if e < n: 
#             n = e
#     for i in range(len(z)):
#         if z[i] == n: 
#             z[i] = c

# def f2(z,c):
#     z[np.argmin(z)] = c

# x = np.array([6,9,12,3,7,5,0])
# print(f1(x,4))
# print(f2(x,4))

# no.10/11
# import numpy as np
# def f1(x, a, b): 
#     # x เป็น 1-D numpy array of ints, a และ b เป็น int
#     return np.array([e for e in x if e < a or e > b])

# def f2(x,a,b):
#     return x[(x < a) | (x > b)]

# x = np.arange(10)
# print(f1(x,4,7))
# print(f2(x,4,7))

# no.11/11
# class A: 
#     def __init__(self, a, b):
#         self.s = [a,b]
#     def __str__(self):
#         return ':'.join([(' '+str(e))[-2:] for e in self.s])
#     def __lt__(self, a):
#         return abs(self.s[0]) + self.s[1] > abs(a.s[0]) + a.s[1]

# a1 = A(9,0)
# a2 = A(-9,-1)
# a3 = A(3,4)
# a4 = A(-8,5)
# for a in sorted([a1,a2,a3,a4]):
#     print(a)