x = input()
index = int(input())
x = x[1:-1].split("||")
z = x.pop(index-1)
print("|"+z+"|")
print("|"+x[0]+"|"+"|"+x[1]+"|"+"|"+x[2]+"|")
