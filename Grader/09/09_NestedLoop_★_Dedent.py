n = int(input())
l = []
for i in range(n):
    s = input()
    if len(s) != 0:
        if s[0] != ".":
            l.append(s)
        else:
            idx = 0
            while s[idx] == ".":
                idx += 1
            st = "."*(idx//2) + s[idx:]
            l.append(st)
    else:
        l.append('')

for i in l:
    print(i)
