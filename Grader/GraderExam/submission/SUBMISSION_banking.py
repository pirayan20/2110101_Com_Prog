n = int(input().strip())
id2name = {}
id2money = {}

for i in range(n):
    s = input().split()
    name,id,money = s[0],s[1],float(s[2])
    id2money[id] = money
    id2name[id] = name

while True:
    s = input().split()
    if s[0] != 'exit':
        which = s[2]

        if which == 'deposit':
            name,id,intake = s[0],s[1],float(s[3])
            if id not in id2name:
                id2name[id] = name
                id2money[id] = 0
            if name != id2name[id]:
                print('Transaction Failed')
            else:
                id2money[id] += intake
                if id2money[id] % 1 == 0:
                    id2money[id] = int(id2money[id])
                print(name,'('+id+')', str(id2money[id]))
        
        elif which == 'withdraw':
            name,id,takeout = s[0],s[1],float(s[3])
            if id not in id2name:
                print('Transaction Failed')
            elif name != id2name[id]:
                print('Transaction Failed')
            else:
                if takeout > id2money[id]:
                    print('Transaction Failed')
                else:
                    id2money[id] -= takeout
                    if id2money[id] % 1 == 0:
                        id2money[id] = int(id2money[id])
                    print(name,'('+id+')', str(id2money[id]))

        elif which == 'transfer':
            name,id,target,transfer = s[0],s[1],s[3],float(s[4])
            if id not in id2name or target not in id2name:
                print('Transaction Failed')
            elif name != id2name[id]:
                print('Transaction Failed')
            elif transfer > id2money[id]:
                print('Transaction Failed')
            else:
                id2money[id] -= transfer
                id2money[target] += transfer
                if id2money[id] % 1 == 0:
                    id2money[id] = int(id2money[id])
                if id2money[target] % 1 == 0:
                    id2money[target] = int(id2money[target])
                print(name,'('+id+')', str(id2money[id]))
                print(id2name[target],'('+target+')', str(id2money[target]))

    else:
        break