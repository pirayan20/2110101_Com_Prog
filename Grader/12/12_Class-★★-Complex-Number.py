class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def __str__(self):
        if float(self.img) == 1.0 or float(self.img) == 0.0 or float(self.img) == -1.0:
            if int(self.real) != 0:
                if int(self.img) == 1:
                    return  str(self.real)+'+'+ "i"
                elif int(self.img) == -1:
                    return str(self.real)+'-'+ "i"
                else:
                    return  str(self.real)
            else:
                if int(self.img) == 1:
                    return  "i"
                elif int(self.img) == -1:
                    return "-i"
                else:
                    return  "0"

        elif float(self.real) == 0:
            return str(self.img) + 'i'
        elif float(self.img) < 0 :
            return str(self.real)+ str(self.img)+"i"
        else:
            return str(self.real)+'+'+ str(self.img)+"i"

    def __add__(self,x):
        newreal = int(self.real) + int(x.real)
        newimg = int(self.img) + int(x.img)
        return str(Complex(newreal,newimg))
        
    def __mul__(self,x):
        newreal = (int(self.real)*int(x.real)) - (int(self.img) * int(x.img))
        newimg = (int(self.real)*int(x.img)) + (int(self.img)*int(x.real))
        return str(Complex(newreal,newimg))

    def __truediv__(self,x):
        newreal = ((int(self.real)*int(x.real)) + (int(self.img) * int(x.img))) /\
            (int(x.real) ** 2 + int(x.img) ** 2)
        newimg = ((int(self.img)*int(x.real)) - (int(self.real)*int(x.img))) /\
            (int(x.real) ** 2 + int(x.img) ** 2)
        return str(Complex(newreal,newimg))

t, a, b, c, d = [int(x) for x in input().split()]

c1 = Complex(a,b)
c2 = Complex(c,d)

if t == 1 :
    print(c1)
elif t == 2 :
    print(c2)
elif t == 3 : 
    print(c1+c2)
elif t == 4 : 
    print(c1*c2)
else : 
    print(c1/c2)

