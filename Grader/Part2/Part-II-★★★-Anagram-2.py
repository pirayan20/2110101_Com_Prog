import string
s1 = input().strip()
s2 = input().strip()


def replace(s):
    for i in string.punctuation:
        s = s.replace(i, "")
    s = s.replace(" ", "")
    return s


def dictRLE(s):
    i = 0
    d = {}
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
        d[alpha] = count
        i = k+1
    return d


d1 = dictRLE(sorted(replace(s1.lower())))
d2 = dictRLE(sorted(replace(s2.lower())))

del1 = []
del2 = []
same = False

l1 = list(d1.keys())
l2 = list(d2.keys())

for i in l1:
    if i not in l2:
        d2[i] = 0

for i in l2:
    if i not in l1:
        d1[i] = 0


if d1 != d2:
    for i in d1:
        for j in d2:
            if i == j:
                remove = 0
                if d1[i] == d2[j]:
                    pass
                elif d1[i] > d2[j]:
                    remove = d1[i] - d2[j]
                    del1.append([i, remove])
                else:
                    remove = d2[i] - d1[j]
                    del2.append([i, remove])
else:
    same = True

if same == False:
    del1 = sorted(del1)
    del2 = sorted(del2)
    print(s1)
    if del1 != []:
        for i in range(len(del1)):
            si = ''
            alpha, count = del1[i][0], del1[i][1]
            if count > 1:
                alpha = alpha + "'s"
            si += " - remove " + str(count) + " " + alpha
            print(si)
    else:
        print(" - None")

    print(s2)
    if del2 != []:
        for i in range(len(del2)):
            si = ''
            alpha, count = del2[i][0], del2[i][1]
            if count > 1:
                alpha = alpha + "'s"
            si += " - remove " + str(count) + " " + alpha
            print(si)
    else:
        print(' - None')
else:
    print(s1)
    print(" - None")
    print(s2)
    print(" - None")
