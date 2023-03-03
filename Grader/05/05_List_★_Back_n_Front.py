q1 = int(input())
num = []
new = []
for i in range(q1):
    s1 = input()
    num.append(s1)

q2 = input()
q2 = q2[0::].split(" ")

for i in range(len(q2)):
    if q2[i] == "":
        pass
    else:
        num.append(q2[i])

while True:
    q3 = input()
    if q3 != "-1":
        num.append(q3)
    else:
        break

for i in range(len(num)):
    num[i] = int(num[i])
    if i % 2 == 0:
        new.append(num[i])
    else:
        new.insert(0, num[i])

print(new)
