
count = 0
for j in range(1,5):
    for i in range(1,10001):
        if "0"*j in str(i):
            count += 1

print(count)