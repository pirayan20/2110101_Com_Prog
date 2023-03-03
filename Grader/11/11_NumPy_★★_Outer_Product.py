import numpy as np

def mult_table(nrows, ncols):
    rows = np.arange(1,nrows+1)
    cols = np.arange(1,ncols+1)
    cols = cols.reshape((cols.shape[0],1))
    return (cols*rows).T

exec(input().strip())