import numpy as np

# ความเจ๋งคือ dot สามารถส่งเป็นลิสต์ให้ได้เลย 
# โดยที่ np จะแปลงให้เองอัตโนมัติ แต่คำสั่งอื่นต้องเป็น array ก่อน

# 1.vector-vector
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.dot(a,b))

# 2.vector-matrix
# ต้องเลือก pattern ในการวางข้อมูลให้ดี ถ้าวางไม่ดีบางครั้งจะ dot ไม่ได้
c = np.array([[4,5,6],[7,8,9]])
d = np.array([[1,3,5],[2,4,6]])
c,d = c.T,d.T
print(np.dot(a,c))                  # แค่ลองสลับ a,c ก้ dot ไม่ได้ละ เพราะงั้นเลือกดีๆ
print(np.dot(d,a[1:]))

# 3.matrix-matrix
# เป็นการคูณ matrix return เป็น matrix
c = c.T
print(d.dot(c))
# print(d@c) เขียนงี้ได้