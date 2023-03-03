from os import path
file = input().strip()
cmd = input().strip()

if cmd not in ['LSTRIP','RSTRIP','STRIP','STRIP_ALL']:
    print('Invalid command')
    exit(0)

file_dir = path.join("C:\\Users\\piray\\Desktop\\File\\Code\\Comprog_ENC\\Grader\\Part3")
filename = path.join(file_dir,file)


# อ่านแต่ละบรรทัดในแฟ้มมาเพื่อหาความกว้างของช่องว่างทางขอบซ้ายและขอบขวา
fn = open(filename)
left_margin = 99999 # ให้ช่องว่างทางขอบซ้ายมีค่ามาก ๆ ไว้ก่อน
right_margin = 99999
for line in fn:
    line = line.strip()
    for left in range(len(line)):
        if line[left] != '.':
            break
    if left < left_margin: left_margin = left

    for right in range(len(line)):
        if line[-right] != '.':
            right -= 1
            break
    if right < right_margin: right_margin = right

fn.close()

if cmd != 'STRIP_ALL':
    fn = open(filename)
    if cmd == 'LSTRIP':
        line = fn.readline()
        while line:
            line = line.replace('\n','')
            print(line[left_margin:].strip())
            line = fn.readline()
        fn.close()

    elif cmd == 'RSTRIP':
        for line in fn:
            line = line.replace('\n','')
            print(line[:-right_margin].strip())
        fn.close()
        
    elif cmd == 'STRIP':
        for line in fn:
            line = line.replace('\n','')
            print(line[left_margin:-right_margin].strip())
        fn.close()

else:
    fn = open(filename)
    pos = []
    for line in fn:
        k = len(line) - 1
        k -= (left_margin+right_margin)
        break
    fn.close()
    for i in range(k):
        valid = True
        fn = open(filename)
        for line in fn:
            line = line.replace('\n','')
            line = line[left_margin:-right_margin]
            if line[i] != '.':
                valid = False
                break
        if valid == True:
            pos.append(i)
        fn.close()
    pos.insert(0,-1)
    
    fn = open(filename)
    for line in fn:
        s = ''
        line = line.replace('\n','')
        line = line[left_margin:-right_margin]
        for i in range(len(pos)):
            if i != len(pos)-1:
                s += line[pos[i]+1:pos[i+1]]
            else:
                s += line[pos[i]+1:]
        print(s.strip())
    fn.close()