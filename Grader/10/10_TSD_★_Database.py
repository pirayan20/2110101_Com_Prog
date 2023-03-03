fcourse = open(input().strip(),'r')
fteacher = open(input().strip(),'r')
fdata = open(input().strip(),'r')

dcourse = {}
dteacher = {}

for line in fcourse:
    num,id = line.strip().split(',')
    dcourse[num] = id
fcourse.close()

for i in fteacher:
    num,id = i.strip().split(',')
    dteacher[num] = id
fteacher.close()

for i in fdata:
    subj,teach = i.strip().split(",")
    if subj in dcourse and teach in dteacher:
        print(dcourse[subj]+','+dteacher[teach])
    else:
        print("record error")

fdata.close()
