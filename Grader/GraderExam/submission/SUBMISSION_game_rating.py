n = int(input().strip())
song2lvl = {}
song2score = {}
song2rate = {}

def rating(lvl,score):
    return int(25*(lvl+1)*(score/(10**7)) // 1)

for i in range(n):
    s = input().split(' | ')
    if s[0] == 'Play':
        name,lvl,score = s[1],int(s[2]),int(s[3])

        if name not in song2score:
            song2score[name] = score
            song2lvl[name] = lvl
            song2rate[name] = rating(lvl,score)

        if rating(lvl,score) > song2rate[name]:
            song2score[name] = score
            song2lvl[name] = lvl
            song2rate[name] = rating(lvl,score)

        elif rating(lvl,score) == song2rate[name]:
            if lvl > song2lvl[name]:
                song2score[name] = score
                song2lvl[name] = lvl
                song2rate[name] = rating(lvl,score)
            elif lvl == song2lvl[name]:
                if score > song2score[name]:
                    song2score[name] = score
                    song2lvl[name] = lvl
                    song2rate[name] = rating(lvl,score)

    elif len(s) == 1:
        l = sorted(list(song2rate.values()))[::-1]
        if len(l) != 0:
            if len(l) >= 5:
                l = l[:5]
            print(sum(l))
        else:
            print('0')

    elif s[0] == 'Rating':
        name = s[1]
        if name not in song2rate:
            print('0')
        else:
            print(song2rate[name])

    elif s[0] == 'Detail':
        name = s[1]
        if name not in song2score:
            print(name+': No play history')
        else:
            print(name + ' | '+ str(song2lvl[name]) + ' | ' + str(song2score[name]) + ' | ' + str(song2rate[name]))