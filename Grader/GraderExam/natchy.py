row,col = [int(e) for e in input().split()]
l = []

for i in range(row) :
    l1 = []
    x = input()

    for i in x :
        l1.append(i)

    l.append(l1)
x = input()
l_index = []

for i in x :
    n = 0
    for j in range(len(l)) :

        for k in range(len(l[j])) :

            if l[j][k] == i and n == 0 :
                if l_index == []:
                    l_index.append((j,k))
                    l[j][k] = ''
                    n += 1
                else :
                    s = j-l_index[-1][0] + k-l_index[-1][1]
                    if s == 1 or s == -1 :
                        l_index.append((j,k))
                        l[j][k] = ''
                        n += 1

                        
print(l_index)