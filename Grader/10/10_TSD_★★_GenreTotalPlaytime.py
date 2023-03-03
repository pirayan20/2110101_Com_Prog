n = int(input().strip())
d = {}
for i in range(n):
    s = input().split(',')
    genre,time = s[2],s[3]  
    min,second = time.split(':')
    time = int(min)*60 + int(second)
    if genre not in d:
        d[genre] = time
    else:
        d[genre] += time

l = []
for i in d:
    time = d[i]
    min = time//60
    second = time - min*60
    if second < 10:
        l.append((min,"0"+str(second),i))
    else:
        l.append((min,str(second),i))

l = sorted(l)[::-1]

if len(l) < 3:
    for i in range(len(l)):
        print(l[i][2],'-->',str(l[i][0])+':'+str(l[i][1]))
else:
    for i in range(3):
        print(l[i][2],'-->',str(l[i][0])+':'+str(l[i][1]))
