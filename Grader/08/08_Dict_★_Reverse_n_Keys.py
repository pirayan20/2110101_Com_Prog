def reverse(d):
    m = {}
    for i in d:
        m[d[i]] = i
    return m


def keys(d, v):
    l = []
    for e in d:
        if d[e] == v:
            l.append(e)
    return l


exec(input().strip())
