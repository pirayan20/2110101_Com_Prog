import numpy as np

def eq(A,B,p):
    k = len(A[A==B])
    return (k/A.size*100) >= p

def closest_point_indexes(points, p):
    dist = np.sqrt((p[0] - points[:,0])**2 + (p[1] - points[:,1])**2)
    mini = min(dist)
    arr = dist[:] == mini
    pos = np.arange(arr.shape[0])
    return pos[arr]

def number_of_inversions(A):
    count = 0
    for i in range(A.size):
        count += np.less(A[i:],A[i]).sum()
    return count

exec(input().strip())
