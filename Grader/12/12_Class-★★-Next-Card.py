val = ["3", "4", "5", "6", "7", "8", "9", "10","J","Q","K","A","2"]
kind = ['club','diamond','heart','spade']

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __str__(self):
        return "(" + str(self.value) + " " + str(self.suit) + ')'

    def next1(self):
        if self.suit == "spade":
            newSuit = "club"
            if self.value == "2":
                newVal = "3"
            else:
                newVal = val[val.index(self.value) + 1]
        else:
            newSuit = kind[kind.index(self.suit) + 1]
            newVal = self.value
        return Card(newVal,newSuit)

    def next2(self):
        d = self.next1()
        self.suit = d.suit
        self.value = d.value


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
