x = int(input())
if x > 0:
    if x % 2 == 0:
        print("positive\neven")
    else:
        print("positive\nodd")
elif x < 0:
    if x % 2 == 0:
        print("negative\neven")
    else:
        print("negative\nodd")
else:
    print("zero\neven")
