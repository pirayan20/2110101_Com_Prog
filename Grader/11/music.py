import numpy as np

def f1(v):
    x = np.arange(v.shape[0])
    y = np.array(x==v)
    if False in y:
        return False
    return True

def f2(u,v):
    return u[:] + v[::-1]

def f3(M,v):
    return M*v


a = np.array([0,1,2,3])
b = np.array([3,6,9,12])
print(f1(a))


# for k in range(int(input())):
#     exec(input().strip())
