m = input()
n = int(input())

x = len(m)

if n > x:
    print("0"*(n-x)+m)
else:
    print(m)
