import numpy as np

def get_column_from_bottom_to_top(A,c):
    A = A.T
    return A[c][::-1]

def get_odd_rows(A):
    return A[1::2]

def get_even_column_last_row(A):
    return A[len(A)-1,::2]

def get_diagonal1(A):
    n = A.shape[0]
    arr = A*np.identity(n,int)
    return arr[arr>0]

def get_diagonal2(A):
    n = A.shape[0]
    iden = np.identity(n,int)
    arr = A*iden[:,::-1]
    return arr[iden[:,::-1]>0]

exec(input().strip())