import numpy as np

# การคำนวณกันแบบ element-wise แต่ขนาดของสอง array มีไม่เท่ากัน
# ระบบจะแก้ขนาดเรียก Broadcast ให้ array ตัวเล็กกลายเป็นตัวใหญ่

a = np.array([2,3])                         
b = np.array([[1,2],[3,4],[5,6]])

# print(a+b)                  # ระบบจะ Broadcast ให้ a มีมิติเท่ากับ b
                            # แต่ในกรณีนี้ทำได้เพราะตอนเป็น vector มีหลักคือ 2
                            # บางครั้งไม่สามารถ broadcast ได้ต้องระวัง
                        

u = np.array([[1,2,3,4]])     # สามารถ broadcast ทั้งสองตัวได้ด้วย!!!
u = u.T                       # ลอง Debug เอา
v = np.array([4,5])
print(u)
print(v)
print(u+v)