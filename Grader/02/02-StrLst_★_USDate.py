x = input()
x = (x[0::].split("/"))
y = ["January", "Februray", "March", "April", "May",
     "June", "July", "August", "September", "October", "November", "December"]
d = x[0]
m = y[int(x[1])-1]
y = x[2]
print(m, d+",", y)
