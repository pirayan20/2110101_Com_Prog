n = int(input())
id2name = {}
id2money = {}

for i in range(n):
    s = input().split()
    name,bankid,money = s[0],s[1],float(s[2])
    id2name[bankid] = name
    id2money[bankid] = money

while True:
    s = input().strip()
    if s != 'exit':
        s = s.split()
        if len(s) == 4:
            name,bankid,cmd,cash = s[0],s[1],s[2],float(s[3])
            if cmd == 'deposit':
                if bankid not in id2money:
                    id2name[bankid] = name
                    id2money[bankid] = 0
                if id2name[bankid] != name:
                    print("Transaction Failed")
                else:
                    id2money[bankid] += cash
                    if id2money[bankid] %1 == 0:
                        id2money[bankid] = int(id2money[bankid])
                    print(id2name[bankid],'('+bankid+")",str(id2money[bankid]))
                    
            elif cmd == 'withdraw':
                k = id2money[bankid]
                if k - cash < 0:
                    print("Transaction Failed")
                else:
                    id2money[bankid] -= cash
                    if id2money[bankid] %1 == 0:
                        id2money[bankid] = int(id2money[bankid])
                    print(id2name[bankid],'('+bankid+")",str(id2money[bankid]))

        elif len(s) == 5:
            name,bankid,cmd,target,cash = s[0],s[1],s[2],s[3],float(s[4])
            if id2name[bankid] != name:
                print("Transaction Failed")
            else:
                k = id2money[bankid]
                if k - cash < 0:
                    print("Transaction Failed")
                else:
                    id2money[bankid] -= cash
                    id2money[target] += cash
                    if id2money[bankid] %1 == 0:
                        id2money[bankid] = int(id2money[bankid])
                    if id2money[target] %1 == 0:
                        id2money[target] = int(id2money[target])
                    print(id2name[bankid],'('+bankid+")",str(id2money[bankid]))
                    print(id2name[target],'('+target+")",str(id2money[target]))
    else:
        break