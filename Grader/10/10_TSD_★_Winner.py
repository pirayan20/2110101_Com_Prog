n = int(input())
l = []
swinner = set()
sloser = set()
for i in range(n):
    winner, loser = input().split()
    swinner.add(winner)
    sloser.add(loser)

for i in swinner:
    if i not in sloser:
        l.append(i)

print(sorted(l))
