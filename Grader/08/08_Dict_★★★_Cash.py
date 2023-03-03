def total(pocket):
    sum = 0
    for e in pocket:
        sum += e*pocket[e]
    return sum


def take(pocket, money_in):
    d = dict(pocket)
    for e in d:
        for i in money_in:
            if e == i:
                pocket[e] += money_in[i]
            else:
                pocket[i] = money_in[i]
    return pocket


def pay(pocket, amt):
    a = []
    for i in pocket:
        a.append(i)
    paid = {}
    for i in a:
        if amt / i >= 1:
            paid[i] = amt//i
            amt -= i*paid[i]
    if total(pocket) - total(paid) < 0:
        return {}
    elif total(pocket) - total(paid) == 0:
        for i in paid:
            for j in pocket:
                if i == j:
                    pocket[i] -= paid[i]
        return paid
    else:
        d = dict(pocket)
        for i in paid:
            for j in d:
                if i == j:
                    d[i] -= paid[i]
                    if d[i] < 0:
                        return {}
        for i in paid:
            for j in pocket:
                if i == j:
                    pocket[i] -= paid[i]
        return paid


# exec(input().strip())


def _a(p):
    print([(k,v) for k,v in sorted(p.items())])

p={}
take(p,{100:2, 1:3})
_a(p)