import numpy as np

N = int(input())
M = int(input()) #จำนวนที่ต้องเรียงกันถึงจะชนะ
board = []

for i in range(N):
    s = [int(e) for e in input().split()]
    board.append(s)

board = np.array(board)
l = np.array([0,1,2])
diff = np.setdiff1d(board,l)
if len(diff) > 0:
    print('ERROR')
    exit(0)

def check_horizontal(board,M):
    player1 = False
    player2 = False
    for i in range(len(board)):
        for j in range(len(board)-M+1):
            s = board[i][j:j+M]
            idx1 = s[0]
            if np.all(s[0]==s) == True:
                if idx1 == 1:
                    player1 = True
                    break
                elif idx1 == 2:
                    player2 = True
                    break
    return player1,player2

def check_vertical(board,M):
    k = board.T
    return check_horizontal(k,M)

def check_diagonal(board,M):
    player1 = False
    player2 = False
    for i in range(len(board)-M+1):
        if i == 0:
            s = np.diag(board)
            for j in range(len(s)-M+1):
                k = s[j:j+M]
                idx1 = k[0]
                if np.all(k[0]==k) == True:
                    if idx1 == 1:
                        player1 = True
                        break
                    elif idx1 == 2:
                        player2 = True
                        break
        else:
            s1 = np.diag(board,i)
            for j in range(len(s1)-M+1):
                k = s1[j:j+M]
                idx1 = k[0]
                if np.all(k[0]==k) == True:
                    if idx1 == 1:
                        player1 = True
                        break
                    elif idx1 == 2:
                        player2 = True
                        break
        
            s2 = np.diag(board,-i)
            for j in range(len(s2)-M+1):
                k = s2[j:j+M]
                idx1 = k[0]
                if np.all(k[0]==k) == True:
                    if idx1 == 1:
                        player1 = True
                        break
                    elif idx1 == 2:
                        player2 = True
                        break
        
    return player1,player2

p1,p2 = check_vertical(board,M)
if not p1 and not p2:
    p1,p2 = check_horizontal(board,M)
if not p1 and not p2:
    p1,p2 = check_diagonal(board,M)
if not p1 and not p2:
    p1,p2  = check_diagonal(np.rot90(board),M)

##############################################

if not p1 and not p2:
    if np.any(np.isin(board,0)) == True:
        print('NOT OVER')
    else:
        print('DRAW')
    
elif p1 and p2:
    print('ERROR')

elif p1:
    print('1 WIN')

else:
    print('2 WIN')