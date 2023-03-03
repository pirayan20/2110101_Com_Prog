m = int(input())
i = 0
point1 = 0
point2 = 0

while i < 3*m:
    if point1 < m and point2 < m:
        s = input().split(" ")
        if s[0] == s[1]:
            i += 1

        elif s[0] == "R":
            if s[1] == "P":
                point2 += 1
            elif s[1] == "S":
                point1 += 1
            i += 1

        elif s[0] == "P":
            if s[1] == "R":
                point1 += 1
            elif s[1] == "S":
                point2 += 1
            i += 1

        elif s[0] == "S":
            if s[1] == "R":
                point2 += 1
            elif s[1] == "P":
                point1 += 1
            i += 1

    elif point2 == m:
        print(point1, point2)
        print("Player 2 wins")
        break

    elif point1 == m:
        print(point1, point2)
        print("Player 1 wins")
        break

if point1 < m and point2 < m:
    print(point1, point2)
    print("Tie")
else:
    pass
