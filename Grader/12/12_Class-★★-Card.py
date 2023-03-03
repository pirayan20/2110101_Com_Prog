class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "(" + str(self.value) + " " + str(self.suit) + ')'
    
    def getScore(self):
        alpha = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        special = ["J","Q","K"]
        if self.value in alpha:
            return alpha.index(self.value) + 1
        elif self.value in special:
            return 10

    def sum(self,other):
        return (self.getScore() + other.getScore()) % 10

    def __lt__(self,rhs):
        val = ["3", "4", "5", "6", "7", "8", "9", "10","J","Q","K","A","2"]
        kind = ['club','diamond','heart','spade']
        if self.value != rhs.value:
            if val.index(self.value) > val.index(rhs.value):
                return False
            else:
                return True
        else:
            if kind.index(self.suit) > kind.index(rhs.suit):
                return False
            else:
                return True


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])