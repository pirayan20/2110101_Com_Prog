def func(x,y,coor_list,key,a,tb): #x,y list of coor
    if a == len(key):
        print(coor_list)
        return
    if x-1 >= 0:
        if tb[x-1][y] == key[a]:
            func(x-1,y,coor_list+[(x-1,y)],key,a+1,tb)
    if y-1 >= 0:
        if tb[x][y-1] == key[a]:
            func(x,y-1,coor_list+[(x,y-1)],key,a+1,tb)
    if x+1 < len(tb):
        if tb[x+1][y] == key[a]:
            func(x+1,y,coor_list+[(x+1,y)],key,a+1,tb)
    if y+1 < len(tb[0]):
        if tb[x][y+1] == key[a]:
            func(x,y+1,coor_list+[(x,y+1)],key,a+1,tb)
N,M = input().split()
N=int(N);M=int(M)
tb = []
for i in range(N):
    s = input().strip()
    tb.append(s)
key = input().strip()
for i in range(N):
    for j in range(M):
        if tb[i][j] == key[0]:
            func(i,j,[(i,j)],key,1,tb)