n = int(input().strip())
l = []
ans = []

for i in range(n):
    s = tuple(input().split())
    l.append(s)
l.sort()

target = input().split()

for i in l:
    good = True
    for j in target:
        if j not in i[1::]:
            good = False
            break
    if good == True:
        ans.append(i)
    
    
if len(ans) != 0:
    for i in ans:
        print(' '.join(i))
else:
    print('Not Found')