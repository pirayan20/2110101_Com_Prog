class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    
class Rect:
    def __init__(self, p1, p2):
        self.lowerleft = p1
        self.upperright = p2
    def area(self):
        w = self.upperright.x - self.lowerleft.x
        h = self.upperright.y - self.lowerleft.y
        return w*h
    def contains(self,p):
        hTrue = False
        wTrue = False
        if p.x <= self.upperright.x and p.x >= self.lowerleft.x:
            wTrue = True
        if p.y <= self.upperright.y and p.y >= self.lowerleft.y:
            hTrue = True
        if hTrue and wTrue:
            return True
        else:
            return False


x1,y1,x2,y2 = [int(e) for e in input().split()]
lowerleft = Point(x1,y1)
upperright = Point(x2,y2)
rect = Rect(lowerleft, upperright)
print(rect.area()) 
m = int(input())
for i in range(m):
    x,y = [int(e) for e in input().split()]
    p = Point(x,y)
    print(rect.contains(p))