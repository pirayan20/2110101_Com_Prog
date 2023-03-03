import numpy as np

def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]

    return weight, data

def report_lower_than_mean(weight, data):
    adjust = data[:,1::] * weight
    summ = (data[:,1::].sum(axis=0))*weight
    mean = summ.sum() / data.shape[0]
    ans = data[(adjust.sum(axis=1) < mean),0]
    if ans.shape[0] == 0:
        print('None')
    else:    
        print(', '.join([str(e) for e in ans]))

exec(input().strip())