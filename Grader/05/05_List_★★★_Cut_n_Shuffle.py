def Cut(card):
    card = card[0::].split(" ")
    sep = int((len(card)+1)/2)

    card_1 = card[:sep]
    card_2 = card[sep:]

    newcard = []
    for i in range(len(card_2)):
        newcard.append(card_2[i])

    for i in range(len(card_1)):
        newcard.append(card_1[i])

    return(newcard)


def Slices(card):
    card = card[0::].split(" ")
    sep = int((len(card)+1)/2)

    card_1 = card[:sep]
    card_2 = card[sep:]

    newcard = []
    x = 0
    y = 0

    for i in range(len(card)):
        if i % 2 == 0:
            newcard.append(card_1[x])
            x += 1
        else:
            newcard.append(card_2[y])
            y += 1
    return(newcard)


c = input()
command = input()

for i in command:
    s = ""
    if i == "C":
        c = Cut(c)
        for j in range(len(c)):
            if j != (len(c) - 1):
                s += c[j]+" "
            else:
                s += c[j]
        c = s

    elif i == "S":
        c = Slices(c)
        for k in range(len(c)):
            if k != (len(c) - 1):
                s += c[k]+" "
            else:
                s += c[k]
        c = s
    else:
        pass

print(c)
