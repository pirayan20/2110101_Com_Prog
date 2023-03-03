x = ['oh', 'one', 'two', 'three',
     'four', 'five', 'six', 'seven',
     'eight', 'nine', 'thousand', 'million']
d = []
for e in x:
    d.append([0, e])
d.sort()
for i in range(len(x)):
    x[i] = d[i][1]
print(x)
