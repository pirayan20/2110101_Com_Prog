num = 256
l = []
for i in range(1,num+1):
    for k in range(1,num+1):
        if (i+k) > 128:
            l.append((i,k))
    
print(l)