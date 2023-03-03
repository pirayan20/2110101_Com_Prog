l = []

while True:
    s = input().split()
    if len(s) == 1:
        start = [s[0]]
        break
    else:
        l.append((s[0],s[1]))

def find_routes(l,start):
    next = set()
    for i in l:
        for j in start:
            if j in i:
                x = list(i)
                x.remove(j)
                next.add(x[0])
    return next

next = find_routes(l,start)
finish = find_routes(l,next)

ans = next | finish | set(start)
ans = sorted(list(ans))

for i in ans:
    print(i)