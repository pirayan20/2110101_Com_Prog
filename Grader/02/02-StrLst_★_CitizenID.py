x = input()
c = len(x)+1
k = 0
for i in range(0, len(x)):
    k += c*int(x[i])
    c -= 1
n12 = (11 - (k % 11)) % 10
print(x[0] + " " + x[1:5] + " " + x[5:10] + " " + x[10:13] + " " + str(n12))