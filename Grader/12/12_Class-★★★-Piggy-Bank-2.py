class piggybank:
    def __init__(self):
        self.coins = {}
        self.coinsType = []
    def add(self,v,n):
        allcoins = 0
        v = float(v)
        for i in self.coins:
            allcoins += self.coins[i]
        allcoins += n
        if allcoins > 100:
            return False
        else:
            if v not in self.coins:
                self.coins[v] = 0
                self.coinsType.append(v)
            self.coins[v] += n
            return True
    def __float__(self):
        value = 0
        for i in self.coins:
            value += self.coins[i] * i
        return float(value)
    def __str__(self):
        l = []
        k = sorted(self.coinsType)
        for i in k:
            l.append(str(i)+':'+str(self.coins[i]))
        return '{' + ", ".join(l) +'}'
    
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)