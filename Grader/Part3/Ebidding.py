n = int(input())
player_bid = {}
winner_bid = {}

for i in range(n):
    s = input().split()
    if s[0] == "B":
        d = {}
        player,item,money = s[1],s[2],int(s[3])
        if item not in player_bid:
            player_bid[item] = []
        player_bid[item].append((player,money))

    elif s[0] == "W":
        player,item = s[1],s[2]
        if item not in player_bid:
            pass
        else:
            l = player_bid[item]
            dic = dict(l)
            dic[player] = 0
            player_bid[item] = list(dic.items())
                

for item in player_bid:
    maxi = 0
    winner = []
    for player,money in player_bid[item]:
        if player not in winner_bid:
            winner_bid[player] = []
        if money > maxi:
            maxi = money
            winner.append(player)
    if len(winner) != 0:
        winner_bid[winner[0]].append((item,maxi))


winner_bid = sorted(list(winner_bid.items()))
for bidder,winprize in winner_bid:
    total = 0
    allprize = []
    if len(winprize) != 0:
        for prize,money in winprize:
            total += money
            allprize.append(prize)
        allprize.sort()
        print(bidder+': $'+str(total) + " -> "+' '.join(allprize))
    else:
        print(bidder+': $0')

