# numpy
import numpy as np

# สร้างarray
a = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]], int)
b = np.ndarray((2, 3), str)  # ((row,col),class)
c = np.zeros((2, 3), int)
d = np.ones((2, 3), int)
I = np.identity(5, int)
x = np.arange(0.0, 1.0, 0.1)  # (เริ่ม,สิ้นสุด,เพิ่มทีละ)
z = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

#ก็อปarray
e = np.zeros_like(d, float)
f = np.ones_like(d, float)

# หาและเปลี่ยนขนาด
a.shape  # (3,4)
a.shape[0]  # 3
a.shape[1]  # 4
len(a.shape)  # 2(ขนาดมิติ)
a.reshape(4, 3)
b.T  # transpose
a[2, 2] == a[(2, 2)]  # True
a[::, ::]  # [row,collumn]เอาช่องเดี่ยวได้
# z=[0,10,20,30,40,50,60,70,80,90]
z[[8, 9, 1]]  # หยิบตำแหน่งเดี่ยวหรือหลายๆอันได้
z = [[False, True, False, ...]]  # จะคืนตำแหน่งที่Trueมา

# คำณวณใช้คำสั่งครอบarrayได้
alog=np.log10(a)
arad=np.radians(a)
asin=np.sin(a)
a = a>=1 #คืนarrayของTrue False

#เครื่องหมาย
and = &
or = |
not = ~
a[(2<a) & (a<5)] #ใช้ได้แค่แบบนี้ถ้าเอาวงเล็บออก=ผิด

# convert the index into a list
idx.tolist()
# ฟังชั่นตย.+
np.delete(array,indextodel,axis) #!!!axis1=colomn axis0=row axisเฉยๆ=row+col
                                #!!!ถ้าเป็นsum axis0=colomn axis1=row
np.equal
np.size
np.sign
np.chararray
np.dtype
np.diff
np.sum
np.less
np.max,np.argmax
np.min,np.argmin
np.mean,np.std
np.dot
def all_pair_distances(points):
    n = len(points)
    X = points[:, 0]
    Y = points[:, 1]
    dX = X-X.reshape(n, 1)
    dY = Y-Y.reshape(n, 1)
    D = (dX**2+dY**2)**0.5
    return D


def count_num(A, num):
    return np.sum(A == num)  # ถ้า A==numจะคืนเป็นarray


count_num(a, 4)  # 2


def get_diagonal(A):
    B = np.arange(0, A.shape[0])
    return A[B, B]
def get_rev_diagonal(A):
    B = np.arange(0, A.shape[0])
    return A[B, B[::-1]]


print(get_diagonal(a))

# transpose เเบบไม่ใช้คำสั่ง
x = np.array([1,2,3,4])
xt = x.reshape((x.shape[0],1))
print(xt,x.T)

#ตัวติดกัน n ตัว
for i in range(len(want_to_check)-n+1) ; n = ความยาวตัวที่อยากเช็ค

#ตาราง สูตรคูณ
def left_pad(n, k):
    return (" "*k +str(n))[-k:]

N = int(input())
k = 2
while k <= N:
    m = 1
    line = ""
    while m <= 5:
        line += left_pad(k*m, 4)
        m += 1
    print(line)
    k += 1

def orthogonal_to_u(vectors, u):
    dotp = np.dot(vectors, u)
    return vectors[dotp == 0]

A = np.array([1,2,3,4])
AT = A.reshape(A.shape[0],1)
print(AT) #คล้ายๆ pattern 6 ใน fill in number

def to_points(grades):
    g = np.array([["A","B+","B","C+","C","D+","D"]])
    p = np.array( [ 4,  3.5, 3,  2.5, 2,  1.5, 1 ] )
    return p.dot(grades==g.T)

# เขียนแบบข้างล่างนี้ก็ได้
#    p  = (grades == 'A' )*4.0
#    p += (grades == 'B+')*3.5
#    p += (grades == 'B' )*3.0
#    p += (grades == 'C+')*2.5
#    p += (grades == 'C' )*2.0
#    p += (grades == 'D+')*1.5
#    p += (grades == 'D' )*1.0
#    return p
    
def gpa(grades, credits):
    points = to_points(grades)
    return np.dot(points, credits)/np.sum(credits)

# s1 เก็บผลรวมของทุกจำนวนใน A
# s2 เก็บอาเรย์ขนาด 8 ช่อง แต่ละช่องเก็บผลรวมของแต่ละคอลัมน์ใน A
# m3 เก็บอาเรย์ขนาด 10 ช่อง แต่ละช่องเก็บค่ามากสุดของแต่ละแถวใน A
# m4 เก็บอาเรย์ขนาด 8 ช่อง แต่ละช่องเก็บอินเด็กซ์ของแถวที่มีค่ามากสุดของแต่ละคอลัมน์ใน A
# a5 เก็บอาเรย์ขนาด 10 ช่อง แต่ละช่องเก็บค่าเฉลี่ยของจำนวนในแต่ละแถวของ A
s1 = np.sum(A)
s2 = np.sum(A, axis=0)
m3 = np.max(A, axis=1)
m4 = np.argmax(A, axis=0)
a5 = np.mean(A, axis=1)

# A==B คงไม่ได้
def eq_array(A, B):
    return A.shape == B.shape and \
           np.sum(A!=B) == 0
           
#ฟังก์ชัน z_scores(x) ที่รับ x เป็นอาเรย์มิติเดียวเก็บคะแนน เพื่อคืนอาเรย์หนึ่งมิติที่เก็บค่าคะแนนมาตรฐาน 
# หรือที่เรียกว่า z-score โดยที่ zi = (xi - μ)/σ, μ และ σ คือ ค่าเฉลี่ยและส่วนเบี่ยงเบนมาตรฐานของข้อมูลใน x (ไม่ต้องใช้คำสั่งวงวน)
def z_scores(x):
    return (x - np.mean(x))/np.std(x)

#ฟังก์ชัน nearest(x, e) ที่รับ x เป็นอาเรย์มิติเดียว และ e เป็นจำนวน 
# ฟังก์ชันนี้คืนค่าใน x ที่มีค่าใกล้กับ e ที่สุด เช่น nearest(np.array([10, 30, 3, 4, 9]), 28) จะได้ 30 (ไม่ต้องใช้คำสั่งวงวน)
def nearest(x,e):
    return x[np.argmin(np.abs(x-e))]


def common_items(x1,x2):
    x2_T = x2.reshape((len(x2),1))
    c = np.sum(x1==x2_T, axis=0)
    return x1[c > 0]

#!LEGENDARY COMMAND
#!SORT DICT WITH VALUE
>>> x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
>>> {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}