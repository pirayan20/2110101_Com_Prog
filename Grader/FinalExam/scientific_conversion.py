import string

f = open('data.txt')
for line in f:
    i = 0
    line = line.replace('\n','')
    words = line.split()
    for word in words:
        if word == '':
            pass
        else:
            k = word.strip()
            if k[0] not in string.digits or k[0] == '0':
                pass
            else:
                num = float(k)
                n = len(k)-1
                m = num / (10**(n))
                if m % 1== 0:
                    m = int(m)
                elif len(str(m)) != len(k) + 1:
                    m = str(m) + '0'*(len(k)-len(str(m))+1)
                ans = str(m)+'E'+str(int(n))
                line = line.replace(word,ans)
    print(line)