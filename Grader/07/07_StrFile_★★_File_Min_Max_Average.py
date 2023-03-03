filename, year = input().split()
y = year[-2:]
min = 200
max = -200
sum = 0
n = 0
file = open(filename)
for line in file:
    name, score = line.split()
    score = float(score)
    if name[:2] == y:
        if score < min:
            min = score
        if score > max:
            max = score
        sum += score
        n += 1
file.close()
if n == 0:
    print("No data")
else:
    avg = sum/n
    print(min, max, avg)
