class piggybank:
    def __init__(self):
        self.d = {1:0,2:0,5:0,10:0}
    def add1(self,n):
        self.d[1] += n
    def add2(self,n):
        self.d[2] += n
    def add5(self,n):
        self.d[5] += n
    def add10(self,n):
        self.d[10] += n
    def __int__(self):
        value = 0
        for i in self.d:
            value += self.d[i] * i
        return value
    def __lt__(self,rhs):
        if int(self) >= int(rhs):
            return False
        else:
            return True
    def __str__(self):
        k = [1,2,5,10]
        l = []
        for i in k:
            l.append(str(i)+':'+str(self.d[i]))
        return '{' + ", ".join(l) +'}'
        

cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)