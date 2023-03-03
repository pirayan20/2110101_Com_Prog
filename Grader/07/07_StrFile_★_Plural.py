n = input()
v = "a", "e", "i", "o", "u"

if n[-1] == "s":
    n += "es"
elif n[-1] == "x":
    n += "es"
elif n[:-3:-1] == "hc":
    n += "es"
elif n[-1] == "y":
    if n[-2] in v:
        n += "s"
    else:
        n = n.replace("y", "ies")
else:
    n += "s"

print(n)
