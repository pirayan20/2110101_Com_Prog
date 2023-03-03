x = input()
num = ["0", '1', '2', '3', '4', '5', '6', '7', '8', '9']
s = ''
for i in x:
    if i in num:
        num.remove(i)
    else:
        pass

if len(num) != 0:
    for i in range(len(num)):
        if i != len(num)-1:
            s += num[i]+","
        else:
            s += num[i]
else:
    s += "None"

print(s)
