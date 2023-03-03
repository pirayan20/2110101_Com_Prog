import math

def rating(lvl,score):
    return math.floor(25*(lvl+1)*(score/10**7))

d = {}
for i in range(int(input())) :
    x = input().split(' | ')

    if len(x) == 4 :
        m = int(rating(int(x[2]),int(x[3])))
        if x[1] not in d :
            d[x[1]] = [int(x[2]),int(x[3]),m]
        else :
            if m < d[x[1]][2] :
                pass
            elif m == d[x[1]][2] :
                if int(x[2]) < d[x[1]][0] :
                    pass
                elif int(x[2]) == d[x[1]][0] :
                    if int(x[3]) < d[x[1]][1] :
                        pass
                    else :
                        d[x[1]] = [int(x[2]),int(x[3]),m]
                else :
                    d[x[1]] = [int(x[2]),int(x[3]),m]
            else :
                d[x[1]] = [int(x[2]),int(x[3]),m]

    elif len(x) == 1 :
        n = 0
        for i in d :
            n += d[i][2]
        print(n)

    elif len(x) == 2 and x[0] == 'Rating' :
        if x[1] not in d :
            print(0)
        else :
            print(d[x[1]][2])

    elif len(x) == 2 and x[0] == 'Detail' :
        if x[1] not in d :
            print(x[1]+': '+'No play history')
        else :
            print(x[1] + ' | '+ str(d[x[1]][0]) + ' | ' + str(d[x[1]][1]) + ' | ' + str(d[x[1]][2]))