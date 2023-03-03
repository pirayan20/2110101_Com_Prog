import numpy as np

def f1(d):
    arr = ((d[:d.shape[0]-1] < 0) & (0 < d[1:d.shape[0]])) | ((d[:d.shape[0]-1] > 0) & (0 > d[1:d.shape[0]]))
    pos = np.arange(arr.shape[0])
    return pos[arr] + 1

def f2(A,B):
     # A and B: square matrices (2-D numpy arrays) of the same shape
    C = []
    for i in range(A.shape[0]):
        for j in range(A.shape[0]):
            C.append(sum([A[k,i]*B[j,k] for k in range(A.shape[0])]))
    return np.array(C).reshape(A.shape)

def f3(x, y, a, b):
    newy = y.reshape(y.shape[0],1)
    arr = (a+b)/(x**2/a - newy**2/b)
    return arr

x = np.array([[1,2],[2,3]])
y = np.array([[8,7],[6,5]])

print(f2(x,y))

