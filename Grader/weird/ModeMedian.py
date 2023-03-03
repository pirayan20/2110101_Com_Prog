x = input().split()
for i in range(len(x)):
    x[i] = float(x[i])
command = input().strip()
if command == "mean":
    print(sum(x)/len(x))
elif command == "median":
    x = sorted(x)
    where = (len(x)+1)/2
    if where % 1 == 0:
        where = int(where)
        print(x[where-1])
    else:
        lim = (len(x)+1)//2
        if lim < where:
            print((int(x[lim-1])+int(x[lim]))/2)
        else:
            print((int(x[lim-1])+int(x[lim-2]))/2)
else:
    print("Not a command")
