n = int(input().strip())
l = []
allBranch = {}
ans = []
for i in range(n):
    branch,slot = input().split()
    allBranch[branch] = int(slot)

num = int(input().strip())
for i in range(num):
    s = input().split()
    l.append((float(s[1]),s[0],s[2::]))

l = sorted(l)[::-1]
for i in l:
    for j in i[2]:
        if allBranch[j] != 0:
            ans.append([i[1],j])
            allBranch[j] -= 1
            break

ans.sort()

for i in ans:
    print(' '.join(i))