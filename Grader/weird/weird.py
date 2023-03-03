str = input().replace(".", "").split()
str = str[::-1]
s = ''
for i in range(len(str)):
    if i != len(str) - 1:
        s += str[i] + " "
    else:
        s += str[i]

print(s+".")
