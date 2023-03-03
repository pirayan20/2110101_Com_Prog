import string

def convex_polygon_area(p):
    value = 0
    p = p + [p[0]]
    for i in range(len(p)-1):
        value += p[i][0] * p[i+1][1]
    for i in range(len(p)-1):
        value -= p[i][1] * p[i+1][0]
    return abs(value/2)
        
def is_heterogram(s):
    d = s.lower()
    l = []
    for i in d:
        if i in string.ascii_lowercase:
            l.append(i)
    l.sort()
    for i in range(len(l)-1):
        if l[i+1] == l[i]:
            return False
    return True

def replace_ignorecase(s, a, b):
    la = len(a)
    i = 0
    d = ''
    while i < len(s):
        if s[i:i+la].lower() == a.lower():
            d += b
            i += la
        else:
            d += s[i]
            i += 1
    return d

def top3(votes):
    l = []
    for e in votes:
        l.append([-int(votes[e]), e])
    l.sort()
    m = []
    for i in range(3):
        m.append(l[i][1])
    return m

for i in range(2):
    exec(input().strip())