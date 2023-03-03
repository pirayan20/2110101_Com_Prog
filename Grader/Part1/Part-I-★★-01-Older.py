x = input()
y = input()
x = x[0::].split(" ")
y = y[0::].split(" ")

x[2] = int(x[2].replace(",", ""))
y[2] = int(y[2].replace(",", ""))


month = ["January", 'February', 'March', 'April',
         'May', 'June', 'July', 'August', 'September',
         'October', 'November', 'December']


if int(x[3]) < int(y[3]):
    print(x[0])
elif int(x[3]) > int(y[3]):
    print(y[0])
else:
    if x[1] == y[1]:
        if x[2] > y[2]:
            print(y[0])
        elif x[2] < y[2]:
            print(x[0])
        else:
            print(x[0], y[0])
    else:
        k = month.index(x[1])
        m = month.index(y[1])
        if k > m:
            print(y[0])
        if k < m:
            print(x[0])
