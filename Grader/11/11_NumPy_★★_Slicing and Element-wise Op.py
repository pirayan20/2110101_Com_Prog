import numpy as np

def sum_2_rows(M):
    arr = M[::2] + M[1::2]
    return arr

def sum_left_right(M):
    arr = M[:,:int(M.shape[1]/2)] + M[:,int(M.shape[1]/2):]
    return arr
    
def sum_upper_lower( M ):
    arr = M[:int(M.shape[0]/2),:] + M[int(M.shape[0]/2):,:]
    return arr

def sum_4_quadrants(M):
    arr = M[:int(M.shape[0]/2),:int(M.shape[1]/2)] + M[int(M.shape[0]/2):,int(M.shape[1]/2):]\
         + M[:int(M.shape[0]/2),int(M.shape[1]/2):] + M[int(M.shape[0]/2):,:int(M.shape[1]/2)]      
    return arr

def sum_4_cells(M):
    arr = M[::2,::2] + M[::2,1::2] + M[1::2,::2]  + M[1::2,1::2]
    return arr

def count_leap_years(year):
    return sum(((year-543) % 400 == 0) | (((year-543) % 100 != 0) & ((year-543) % 4 == 0)))


exec(input().strip())

