sell = []
item = []
all = 0

while True:
    s = input()
    if s != "q":
        name,price = s.split()
        if name not in item:
            item.append(name)
            sell.append(float(price))
    else:
        break

calc = input().split()

for i in calc:
    all += sell[item.index(i)]

print("Total",str(all))