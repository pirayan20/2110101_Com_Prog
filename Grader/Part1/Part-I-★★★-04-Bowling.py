s = input()
i = 0
count = 0
l = []
n = int(input())

while count != 10:
    if count != 9:
        if s[i] == "X":
            l.append(s[i])
            i += 1
            count += 1
        else:
            l.append(s[i:i+2])
            i += 2
            count += 1
    else:
        l.append(s[i::])
        count += 1


def bowlingscore(list):
    score = []
    for j in range(len(list)):
        if j != 9:
            if list[j] == "X":
                if list[j+1] == "X":
                    if list[j+2] == "X":
                        score.append(30)
                    else:
                        score.append(20+int(list[j+2][0]))
                elif list[j+1][1] == "/":
                    score.append(20)
                else:
                    score.append(10 + int(list[j+1][0]) + int(list[j+1][1]))
            elif list[j][1] == "/":
                if list[j+1] == "X":
                    score.append(20)
                else:
                    score.append(10+int(list[j+1][0]))
            else:
                score.append(int(list[j][0]) + int(list[j][1]))
        else:
            if list[j][0] == "X":
                if list[j][2] == "/":
                    score.append(20)
                elif list[j][1] == "X":
                    score.append(20 + int(list[j][2]))
                else:
                    score.append(10 + int(list[j][1]) + int(list[j][2]))

            elif list[j][1] == "/":
                if list[j][2] == "X":
                    score.append(20)
                else:
                    score.append(10 + int(list[j][2]))
            else:
                score.append(int(list[j][0]) + int(list[j][1]))

    return score


if 0 < n <= 10:
    print(bowlingscore(l)[n-1])
else:
    print(sum(bowlingscore(l)))
