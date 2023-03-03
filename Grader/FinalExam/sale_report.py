n = int(input().strip())
buyer2phone = {}
id2buyer = {}
brand2buyer = {}
for i in range(n):
    firstname,surname,prodid,brand = input().split()
    name = firstname + ' '+ surname
    if name not in buyer2phone:
        buyer2phone[name] = []
    buyer2phone[name].append(prodid + ' '+ brand)
    if prodid not in id2buyer:
        id2buyer[prodid] = []
    id2buyer[prodid].append(name)
    if brand not in brand2buyer:
        brand2buyer[brand] = []
    brand2buyer[brand].append(name)

m = int(input().strip())
for k in range(m):
    s = input().strip()
    if s in buyer2phone:
        print(s + ' --> '+ ', '.join(sorted(buyer2phone[s])))
    elif s in id2buyer:
        print(s + ' --> '+ ', '.join(sorted(id2buyer[s])))
    elif s in brand2buyer:
        print(s + ' --> '+ ', '.join(sorted(brand2buyer[s])))
    else:
        print(s + ' --> Not found')