d = {0:'soon',1:'neung',2:'song',3:'sam',4:'si',5:'ha',6:'hok',7:'chet',8:'paet',9:'kao',10:'sip'}


def to_Thai(n):
    k = n
    out = ''
    if n >= 1000:
        pun = n//1000
        out += d[pun] + ' pun '
        n %= 1000

    if n >= 100:
        roi = n//100
        out += d[roi] + ' roi '
        n %= 100

    if n >= 10:
        sip = n//10
        if sip == 1:
            out += 'sip '
        elif sip == 2:
            out += 'yi sip '
        elif sip == 0:
            pass
        else:
            out += d[sip] + ' sip ' 
        n %= 10

    if n >= 0:
        if k >= 10:
            if n == 1:
                out += 'et'
            elif n == 0:
                pass
            else:
                out += d[n]
        else:
            out += d[n]

    return out.strip()

exec(input().strip())