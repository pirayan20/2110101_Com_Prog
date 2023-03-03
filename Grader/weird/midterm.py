'''
m = input()
kom = True
if m%2==1 and m<8 or m%2==0 and m>7:
    kom = True
else:
    kom = False
print(kom)
'''

'''
c = input()
if c[-2:] == "21":
    print('Yes, an engineering student ID.')
else:
    print('No, this is not an intania ID.')
print(type(c[-2:]))
'''

'''
def grading(s):
    if s >= 80:
        print("A")
    elif s >= 70:
        print("B")
    elif s >= 60:
        print("C")
    elif s >= 50:
        print("D")
    else:
        print("F")


for i in range(5):
    s = float(input())
    grading(s)
'''

x = ['oh', 'one', 'two', 'three',
     'four', 'five', 'six', 'seven',
     'eight', 'nine', 'thousand', 'million']
d = []
for e in x:
    d.append(e)
d.sort()
for i in range(len(x)):
    x[i] = d[i][1]
print(x)
