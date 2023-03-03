a = input()
b = input()
c = 0

if len(a) == len(b):
    for i in range(len(a)):
        if a[i] == b[i]:
            c += 1
        else:
            pass
    print(c)
else:
    print("Incomplete answer")
