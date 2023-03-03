n = int(input())
l = []

for i in range(n):
    s = input().split()
    l.append(s)

cmd = input().split()

if cmd[0] == 'show':
    for i in l:
        print(' '.join(i))

elif cmd[0] == 'get':
    get = False
    for i in l:
        if i[0] == cmd[1]:
            get = True
            print(' '.join(i))
    if get == False:
        print(str(cmd[1]),'not found')

elif cmd[0] == 'avg':
    cmd[1] = int(cmd[1])
    num = 0
    for i in l:
        num += float(i[cmd[1]])
    num /= len(l)
    print(round(num,4))

elif cmd[0] == 'max':
    cmd[1] = int(cmd[1])
    max = ['',0]
    for i in l:
        if float(i[cmd[1]]) > max[1]:
            max = [i[0],float(i[cmd[1]])]

        elif float(i[cmd[1]]) == max[1]:
            if max[0] > i[0]:
                max = [i[0],float(i[cmd[1]])]

    print(' '.join([str(e) for e in max]))

elif cmd[0] == 'sort':
    ans = ''
    cmd[1] = int(cmd[1])
    k = []
    for i in l:
        k.append([i[cmd[1]],i[0]])
    k = sorted(k)
    for i in k:
        ans += i[1] + ' '
    print(ans.strip())
    