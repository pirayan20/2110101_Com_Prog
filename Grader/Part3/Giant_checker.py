import string
position = input().strip()
validRow = True
validCol = True

if len(position) <= 3 :
    row = position[0]
    col = position[1:]

    if row not in string.ascii_letters:
        validRow = False
    
    for i in col:
        if ord(i) == 32:
            pass
        elif ord(i) > 57 or ord(i) < 48:
            validCol = False
            break

    if col == '':
        validCol = False
    
    if validCol:
        if int(col) > 52 or int(col) < 1:
            validCol = False

    if validRow and validCol:
        r = string.ascii_letters.find(row)
        if r%2 == int(col)%2:
            print('Black')
        else:
            print('White')

    elif validRow == False and validCol == True:
        print("Invalid row")

    elif validRow == True and validCol == False:
        print('Invalid column')

    else:
        print('Invalid row and column')

else:
    row = 0