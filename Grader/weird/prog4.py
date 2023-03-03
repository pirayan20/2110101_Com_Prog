data = [['A102', 50], ['A103', 40], ['B014', 40], ['B109', 30]]
use = []
id, point = input().split(",")
for i in range(len(data)):
    use.append(data[i][::-1])

n = 0
while int(point) < use[n][0]:
    n += 1

use.insert(n, [int(point), id])

for i in range(len(use)):
    use[i][0], use[i][1] = use[i][1], use[i][0]
print(use)
