d = {'R':1,'Y':2,'G':3,'W':4,'B':5,'P':6,'K':7}
count,score1,score2 = 0,0,0

while count < 6:
    s = input().strip()
    if len(s) == 2:
        if s[1] != 'X':
            count += 1
            if s[0] == '1':
                score1 += d[s[1]]
            else:
                score2 += d[s[1]]
    elif len(s) == 3:
        if s[0] == '1':
            score1 += 1
            if s[2] != "X":
                score1 += d[s[2]]
        else:
            score2 += 1
            if s[2] != 'X':
                score2 += d[s[2]]
        
print(score1,score2)
if score1 < score2:
    print('Player 2 wins')
elif score1 > score2:
    print('Player 1 wins')
else:
    print('Tie')