import numpy as np
def check_next(lists):
    ans = []
    for idx in lists[0]:
        for i in lists[1]:
            diff = np.abs(idx[0] - i[0]) + np.abs(idx[1] - i[1])
            if diff == 1:
                ans.append([idx,i])
    return ans

all = [[(1, 5), (3, 3), (4, 3)], [(1, 0), (2, 5), (4, 4)], [(2, 6), (3, 5)], [(3, 4)], 
[(1, 0), (2, 5), (4, 4)], [(1, 5), (3, 3), (4, 3)], [(1, 5), (3, 3), (4, 3)], [(2, 2), (3, 2)]]
print(check_next(all))