import numpy as np

a = np.array([1,2,3,4])                     # สร้างจากลิสต์
b = np.array([[1,2],[2,3],[3,4]],float)
c = np.ndarray((2,3),int)                   # สร้างตามขนาด
d = np.zeros((2,3),int)                     # matrix 0
e = np.ones((2,3),float)                    # matrix 1
f = np.zeros_like(c,float)                  # matrix 0; size of c
g = np.ones_like(c,int)                     # matrix 1; size of c
h = np.identity(4,int)                      # identity matrix; size of n
x = np.arange(0.0,1.0,0.2)

print(d.shape[0])                           # คืนเป็น tuple ของมิติ
print(d.shape[1])

z = np.arange(8)
w = z.reshape((4,2))                # เปลี่ยนมิติ ใช้ทำ transpose ปลอมได้
print(w)                            # จะเห็นว่าทำแล้วมิติไม่เท่าเดิม

p = b.T                                     # transpose มิติเดิม
print(b)                                
print(p)