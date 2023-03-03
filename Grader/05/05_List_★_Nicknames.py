realname = ["Robert", "William", "James", "John", "Margaret", "Edward", "Sarah", "Andrew", "Anthony", "Deborah"]
nickname = ["Dick", "Bill", "Jim", "Jack", "Peggy", "Ed", "Sally", "Andy", "Tony", "Debbie"]
used = []

n = int(input())
for i in range(n):
    s = input()
    if s in nickname:
        k = nickname.index(s)
        used.append(realname[k])
    elif s in realname:
        k = realname.index(s)
        used.append(nickname[k])
    else:
        used.append("Not found")

for i in range(len(used)):
    print(used[i])
