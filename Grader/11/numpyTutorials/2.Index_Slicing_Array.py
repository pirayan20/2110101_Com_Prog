import numpy as np

def count_ones(A):
    c = 0
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if A[i,j] == 1:                 # วิธีเรียก index
                c += 1
    return c

a = np.identity(5,int)
print(count_ones(a))


a = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
b = np.array(a)
                                            # เขียนแบบ slicing
print(b[::2,::2])                           # รูปแบบ: A[เลือกแถว,เลือกหลัก]

# fancy indexing
a = np.arange(0,100,10)
b = a[::2]
c = a[[8,1,9,0]]                            # ใส่ index เป็นลิสต์ของ index ที่ต้องการได้
d = c[[True,False,False,True]]              # หรือใส่ค่าความจริงเพื่อเลือกว่าเอาไม่เอาได้
print(c)
print(d)

A = np.array([[1,2,3],[4,5,6],[7,8,9],[0,1,0]])
B = A[[1,3,2],[2,0,1]]                      # ก็จะจับคู่เป็น A[1,2], A[3,0], A[2,1]
print(B)