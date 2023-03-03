'''
day = 'Sun   Mon   Tues  Wednes' + \
      'Thurs Fri   Satur'
d = int(input())
print(day[(d*6):(d*6)+6].strip() + 'day')
# โจทย์ผิดป่าววะ


x = input()
x, s = x.split(':')
b, a = x.split('+')
b, c = b.split('-')
print(a + s + b + s + c)
'''

n = 1
while 19/n * n == 19.0:
    n += 1
print(n)
