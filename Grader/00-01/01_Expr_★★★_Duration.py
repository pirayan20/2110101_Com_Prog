h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
dh = h2 - h1
dm = m2 - m1
ds = s2 - s1
if dh >= 0 and dm >= 0 and ds >= 0:
    print(str(dh)+":"+str(dm)+":"+str(ds))

elif dh < 0 and dm >= 0 and ds >= 0:
    dh = (24 + (dh)) % 24
    print(str(dh)+":"+str(dm)+":"+str(ds))

elif dh >= 0 and dm < 0 and ds >= 0:
    dm = (60 + (dm)) % 60
    dh -= 1
    if dh < 0:
        dh = (24 + (dh)) % 24
        print(str(dh)+":"+str(dm)+":"+str(ds))
    else : print(str(dh)+":"+str(dm)+":"+str(ds))

elif dh >= 0 and dm >= 0 and ds < 0:
    ds = (60 + (ds)) % 60
    dm -= 1
    if dm < 0:
        dm = (60 + (dm)) % 60
        dh -= 1
        if dh < 0:
            dh = (24 + (dh)) % 24
            print(str(dh)+":"+str(dm)+":"+str(ds))
        else : print(str(dh)+":"+str(dm)+":"+str(ds))
    else: print(str(dh)+":"+str(dm)+":"+str(ds))

elif dh >= 0 and dm < 0 and ds < 0:
    ds = (60 + (ds)) % 60
    dm = (60 + (dm)) % 60
    dm -= 1
    dh -= 1
    if dh < 0:
        dh = (24 + (dh)) % 24
        print(str(dh)+":"+str(dm)+":"+str(ds))
    else : print(str(dh)+":"+str(dm)+":"+str(ds))

elif dh < 0 and dm < 0 and ds >= 0:
    dm = (60 + (dm)) % 60
    dh = (24 + (dh)) % 24
    dh -= 1
    print(str(dh)+":"+str(dm)+":"+str(ds))

elif dh < 0 and dm >= 0 and ds < 0:
    ds = (60 + (ds)) % 60
    dh = (24 + (dh)) % 24
    dm -= 1
    if dm < 0:
        dm = (60 + (dm)) % 60
        dh -= 1
        print(str(dh)+":"+str(dm)+":"+str(ds))
    print(str(dh)+":"+str(dm)+":"+str(ds))

else:
    dh = (24 + (dh)) % 24
    dm = (60 + (dm)) % 60
    ds = (60 + (ds)) % 60
    dm -= 1
    dh -= 1
    print(str(dh)+":"+str(dm)+":"+str(ds))
    

   
        
    