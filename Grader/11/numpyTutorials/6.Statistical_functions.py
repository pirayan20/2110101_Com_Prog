import numpy as np

a = np.arange(49)
a = a.reshape((7,7))
print(a)
print(np.sum(a))                        # บอกค่าบวกกันของทุกตัวใน array
print(np.min(a,axis=0))                 # บอกตัวที่น้อยสุดของหลักนั้น ใช้ argmin ได้ตำแหน่ง
print(np.max(a,axis=1))                 # บอกตัวที่มากที่สุดของแถวนั้น argmax ได้ตำแหน่ง
print(np.mean(a,axis=1))                # บอกค่าเฉลี่ย
print(np.std(a))                        # บอกค่าเบี่ยงเบนมาตรฐาน


# รับ argument เป็น axis โดย axis=0 คือแกน Y \\ axis=1 คือแกน X
# return เป็น array