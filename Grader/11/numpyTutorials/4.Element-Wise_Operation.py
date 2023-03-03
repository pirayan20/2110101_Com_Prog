import numpy as np
x = [1,2,3]
y = [4,5,6]
# print(x+y)

u = np.array(x)
v = np.array(y)
w = u + v                               # บวกให้เองทีละตัว เป็น operation ของ array
# print(w)

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
I = np.identity(3,int)
B = I*A                                 # คูณให้เองหมด return array
# print(B)

# Element-Wise Logical operator
# and = "&" \\ or = '|'  \\ not = '~'
a = np.array([9,3,0,2,6])
b = a[a < 5]                            # b = a[[False,True,True,True,False]]
c = a[(2 < a) & (a < 5)]
print(c)                            