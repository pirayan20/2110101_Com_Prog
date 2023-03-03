import string

fname = input().strip()
k = int(input())
ruler = ''
for i in range(k//10) :
    ruler += '-'*9 + str(i+1)
if k % 10 != 0 :
    ruler += '-'*( k % 10 )
print(ruler)

f = open(fname,"r")
s = f.read()
s = s.replace('\n','.')
f.close()

l = s
ans = []
for j in range(int(len(s)//k +1)):
    if len(l) > k:
        if "." not in l:
            ans.append(l)
            l = l[len(l):] 

        elif l[k] == ".":
            ans.append(l[:k].strip("."))
            l = l[k:].strip('.')

        elif l[k] in string.ascii_letters or l[k] in string.digits:
            if l[k-1] != ".":
                m = l[:k-1][::-1]
                idx = m.find(".")
                m = m[idx+1:][::-1]
                ans.append(m)
                l = l.replace(m,'.').strip('.')
            else:
                ans.append(l[:k].strip("."))
                l = l[k:].strip('.')
    elif len(l) == 0:
        break
    else:
        ans.append(l.strip('.'))
            
for i in ans:
    print(i)
