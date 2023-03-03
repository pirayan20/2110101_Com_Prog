num = 10
d ={}
s = ''

#todo1.1
for i in range(2**num):
    head = False
    d[i] = bin(i)[2:]
    if len(d[i]) != 10:
        x = len(d[i]) 
        d[i] = '0'*(10-x) + d[i]

#todo1.2
val = list(d.values())
l = []
count = 0
for i in val:
    if '00' in i :
        count += 1
        l.append(i + ' True Count:' + str(count))
    else:
        l.append(i + ' False')

for i in l:
    print(i)

print('Total probabbilityt:', str(len(val)) + ' probabblities')
print('Find 00:',str(count),'probabbilities')
print('Probabbility of 00 in', str(len(val)),'elements:',str(count/len(val)*100)+'%')
