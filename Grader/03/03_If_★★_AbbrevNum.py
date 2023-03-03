sub = int(input())
if sub < 1000:
    print(sub)
elif 1000 <= sub < 10000:
    sub = round(sub/1000,1)
    print(str(sub)+"K")
elif 10000 <= sub < 10e5:
    sub = sub//10
    print(str(round(sub/100))+"K")
elif 10e5 <= sub < 10e6:
    sub = round(sub/10e5,1)
    print(str(sub)+"M")
elif 10e6 <= sub < 10e8:
    sub = sub//10
    print(str(round(sub/10e4))+"M")
elif 10e8 <= sub < 10e9:
    sub = round(sub/10e8,1)
    print(str(sub)+"B")
elif 10e9 <= sub:
    sub = sub//10
    print(str(round(sub/10e7))+"B")
