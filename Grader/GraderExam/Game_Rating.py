import math
song2score = {}
song2lvl = {}
song2rate = {}

def rate(lvl,score):
    return math.floor(25*(lvl+1)*(score/10**7))

n = int(input())
for i in range(n):
    s = input().split(" | ")
    if s[0] == 'Play':
        name,lvl,score = s[1],int(s[2]),int(s[3])
        if name not in song2score:
            song2score[name] = score
            song2lvl[name] = lvl
            song2rate[name] = rate(song2lvl[name],song2score[name])
        if rate(song2lvl[name],song2score[name]) > song2rate[name]:
            song2rate[name] = rate(song2lvl[name],song2score[name])
            song2lvl[name] = lvl
            song2score[name] = score
        elif rate(song2lvl[name],song2score[name]) == song2rate[name]:
            if lvl > song2lvl[name]:
                song2lvl[name] = lvl
                song2score[name] = score
            elif lvl == song2lvl[name]:
                song2score[name] = score

    elif s[0] == 'Rating' and len(s) == 2:
        name = s[1]
        if name not in song2score:
            print(0)
        else:
            print(song2rate[name])
    elif s[0] == 'Rating':
        total = 0
        for i in song2rate:
            total += song2rate[i]
        print(total)
    else:
        name = s[1]
        if name not in song2rate:
            print(name+': No play history')
        else:
            print(name,'|',song2lvl[name],'|',song2score[name],"|",song2rate[name])