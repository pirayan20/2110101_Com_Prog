
def remove_len1(d):
    s = dict(d)
    for i in s:
        if len(s[i]) == 1:
            d.pop(i)
    return d

def to_type2(type1):
    d = {}
    for i in type1:
        key,value = i.split(":")
        if key not in d:
            d[key] = []
        d[key].append(value)
        if value not in d:
            d[value] = []
        d[value].append(key)
    return d

exec(input().strip())