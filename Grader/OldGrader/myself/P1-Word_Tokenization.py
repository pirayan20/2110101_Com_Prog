before = input().strip().lower()
after = []
dictionary = {}
n = int(input())
for i in range(n):
    s = input().strip()
    dictionary[s] = len(s)

k = before
while len(k) != 0:
    l = []
    for sepword in dictionary:
        if k[:dictionary[sepword]] == sepword:
            l.append(sepword)
    if len(l) == 1:
        after.append(l[0])
        k = k[len(l[0]):]
    elif len(l) > 1:
        ans = ''
        maximum = 0
        for i in l:
            if len(i) > maximum:
                maximum = len(i)
                ans = i
        after.append(ans)
        k = k[len(ans):]
    else:
        after.append(k[0])
        k = k[1:]

answer = ''
i = 0
while i < len(after):
    if after[i] in dictionary:
        answer += after[i] +" "
        i += 1
    else:
        while after[i] not in dictionary:
            answer += after[i]
            i += 1
        answer += ' '

print(answer)