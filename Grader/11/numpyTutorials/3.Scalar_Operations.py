import numpy as np

a = np.zeros(8,int)
a[2:5] = 9
print(a)

b = np.ndarray((4,4),int)
b[:,:] = 9
print(b)

c = np.array([1,2,3,4,5])
print(c+1)                              # จัดการให้กับทุกตัวใน array แล้วคืนค่าแบบเดิม

def toCM(inches):
    return inches * 2.54

d = np.array([0,10,12,100])
print(toCM(d))

# variable in import math also in numpy
print(np.e)
print(np.pi)

# comparing with conditional sentence
e = np.array([1,2,3,4])
f = e > 3                               # เปรียบเทียบให้ตัวต่อตัว return เป็น Boolean array
print(f)