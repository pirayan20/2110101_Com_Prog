import numpy as np

def peak_indexes(x):
    arr = (x[:x.shape[0]-2] < x[1:x.shape[0]-1]) & (x[1:x.shape[0]-1] > x[2:x.shape[0]])
    pos = np.arange(arr.shape[0])
    return pos[arr] + 1

def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")

exec(input().strip())