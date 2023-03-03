class Book:
    def __init__(self,title,isbn,price):
        self.title = title
        self.isbn = isbn
        self.price = price

    def __str__(self):
        return str(self.title)

    def __int__(self):
        return int(self.isbn)

    def __mul__(self,x):
        return int(self.isbn) * int(x.isbn)

    def __lt__(self,x):
        return float((self.price)[:3]) < float((x.price)[:3])

c1 = Book("Helloworld",'2546','500THB')
c2 = Book("helloDarkness",'2544',"400THB")

print(str(c1))

print(c1*c2)
print(c1<c2)


# string boolean integer float-number
a = 1 #integer
b = 0.1 #float

class Car:
    def __init__(self,brand,model,plate,oil):
        self.brand = brand
        self.model = model
        self.plate = plate
        self.oil = oil

    def changeOil(self,newOil):
        self.oil = newOil


d = Car("toyota","camry","UV-871","diesel91")

print(d.oil)
d.changeOil("e20")
print(d.oil)
