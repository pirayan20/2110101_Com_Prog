char = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

class roman:
    def __init__(self,r):
        self.roman = r
        value = 0
        i = 0
        while i <= len(self.roman) -1:
            k = i
            cash = char[self.roman[k]]
            j = 1
            while k < len(self.roman) - 1:
                if self.roman[k] == self.roman[k+1]:
                    j += 1
                    k += 1
                    cash += char[self.roman[k]]
                elif char[self.roman[k]] > char[self.roman[k+1]]:
                    break
                else:
                    cash = char[self.roman[k+1]] - cash
                    k += j
                    break
            value += cash
            i = k+1
        self.value = value

    def parse(self):
        value = self.value
        s = ''
        if value >= 1000:
            pun = value // 1000
            s += "M"*pun
            value %= 1000
        if value >= 100:
            roi = value // 100
            if roi == 9:
                s += 'CM'
            elif roi >= 5:
                s += 'D' + 'C' * int(roi-5)
            elif roi == 4:
                s += 'CD'
            elif roi >= 1:
                s += 'C' * int(roi)
            value %= 100
        if value >= 10:
            sib = value // 10
            if sib == 9:
                s += 'XC'
            elif sib >= 5:
                s += 'L' + 'X' * int(sib-5)
            elif sib == 4:
                s += 'XL'
            elif sib >= 1:
                s += 'X' * int(sib)
            value %= 10
        if value >= 1:
            noi = value // 1
            if noi == 9:
                s += 'IX'
            elif noi >= 5:
                s += 'V' + 'I' * int(noi-5)
            elif noi == 4:
                s += 'IV'
            elif noi <= 3:
                s += 'I' * int(noi)
        return s

    def __lt__(self,rhs):
        if self.value > rhs.value:
            return False
        return True

    def __str__(self):
        return self.roman

    def __int__(self):
        return self.value

    def __add__(self,rhs):
        value = self.value + rhs.value
        k = roman("")
        k.value = value
        k.roman = k.parse()
        return k

t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))
