n = int(input().strip())

price = []

for i in range(n):
    s = input().split(',')
    for e in s:
        price.append(float(e))

if n <= 2:
    print('No results')
    exit(0)

def start_fast_EMA(price):
    l = ['X']*6
    period = 7
    l.append(round(sum(price[:period])/period,3))
    return l

def next_fast_EMA(price,EMA):
    alpha = 2/(1+7)
    next = alpha * price[len(EMA)] + EMA[len(EMA)-1] * (1-alpha)
    EMA.append(round(next,3))

def start_slow_EMA(price):
    l = ['X']*13
    period = 14
    l.append(round(sum(price[:period])/period,3))
    return l

def next_slow_EMA(price,EMA):
    alpha = 2/(1+14)
    next = alpha * price[len(EMA)] + EMA[len(EMA)-1] * (1-alpha)
    EMA.append(round(next,3))

# create a list of both EMA
fast = start_fast_EMA(price)
for i in range(n*7-7):
    next_fast_EMA(price,fast)

slow = start_slow_EMA(price)
for i in range(n*7-14):
    next_slow_EMA(price,slow)

compare = list(zip(fast[14:],slow[14:]))

one = False
slowmore = False
fastmore = False
i = 0

if slow[13] > fast[13]:
    slowmore = True
else: fastmore = True

while slowmore or fastmore:
    if i <= len(compare) - 1:
        if slowmore and compare[i][0] > compare[i][1]:
            one = True
            print('BUY at {:.2f}'.format(price[i+14]))
            i += 1
            slowmore = False
            fastmore = True
        elif fastmore and compare[i][0] < compare[i][1]:
            one = True
            print('SELL at {:.2f}'.format(price[i+14]))
            i += 1
            slowmore = True
            fastmore = False
        else:
            i += 1
    else:
        break

if not one:
    print('No results')