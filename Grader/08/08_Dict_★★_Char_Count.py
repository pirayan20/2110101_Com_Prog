import string
s = input().strip()
for i in string.punctuation:
    s = s.replace(i, "")
s = s.replace(" ", "")
for i in string.digits:
    s = s.replace(i, "")
s = s.lower()
s = sorted(s)


def count(s):
    i = 0
    l = []
    while i <= len(s)-1:
        count = 1
        alpha = s[i]
        k = i
        while k < len(s)-1:
            if s[k] == s[k+1]:
                count += 1
                k += 1
            else:
                break
        l.append([count, alpha])
        i = k+1
    return l


l = count(s)

for e in l:
    e[0] = -e[0]
l = sorted(l)

for i in range(len(l)):
    print(str(l[i][1]), "->", str(l[i][0])[1::])
