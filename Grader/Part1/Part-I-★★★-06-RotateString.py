command = input()
n = int(input())
l = []
for i in range(n):
    s = input().strip()
    l.append(s)

length = []

# --------check for invalid size

for d in range(len(l)):
    x = len(l[d])
    length.append(x)

for k in range(len(length)):
    if length[k-1] == length[k]:
        running = 1
    else:
        running = 0
        print("Invalid size")
        break

# --------check for invalid size

while running == 1:
    if command == "90":
        b = 0
        for i in range(len(l[0])):
            result = ""
            k = n
            for j in range(len(l)):
                k -= 1
                result += l[k][b]
            b += 1
            print(result)
        break

    elif command == "flip":
        for i in range(len(l)):
            result = ""
            result += l[i][::-1]
            print(result)
        break

    elif command == "180":
        l = l[::-1]
        for i in range(len(l)):
            result = ""
            result += l[i][::-1]
            print(result)
        break
