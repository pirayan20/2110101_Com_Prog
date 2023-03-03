import numpy as np
s = input().split()
l = []
    
for i in range(int(s[0])):
    k = []
    for j in input().strip():
        k.append(j)
    l.append(k)

target = input().strip()
m = np.array(l)
all = []

for i in range(len(target)): # get all the index of all character
    char = target[i]
    whr = np.where(m == char)
    charidx = list(zip(whr[0],whr[1]))
    all.append(charidx)

def check(all): # pairing check
    for i in range(len(all)-1):
        strwork = []
        endwork = []
        start = all[i]
        end = all[i+1]
        for d in start:
            for e in end:
                diff = np.abs(d[0] - e[0]) + np.abs(d[1] - e[1]) # check if it was surrounded by the before idx
                if diff == 1:                                    # if surrounded, the sum of index-difference would equal to 1
                    if d not in strwork:
                        strwork.append(d)
                    if e not in endwork:
                        endwork.append(e)
        all[i] = strwork
        all[i+1] = endwork
    return all

for i in range(2): # check both forwards and backwards --> cause its only one path possible, it has to be possible both ways.
    all = check(all)[::-1]

ans = [e for idx in all for e in idx] # to flatten-list
print(ans)