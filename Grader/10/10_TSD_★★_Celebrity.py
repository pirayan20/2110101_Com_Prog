
def knows(R,x,y):
    if x == y:
        return True
    else:
        if y in R[x]:
            return True
        return False


def is_celeb(R,x):
    if R[x] == set() or R[x] == {x}:
        for i in R:
            if knows(R,i,x) == False:
                return False
        return True
    else:
        return False


def find_celeb(R):
    for i in R:
        if is_celeb(R,i) == True:
            return i
    return None


def read_relations():
    R = {}
    while True:
        d = input().split()
        if len(d) == 1:
            break
        else:
            if d[0] not in R:
                R[d[0]] = set()
            elif d[1] not in R:
                R[d[1]] = set()
            R[d[0]].add(d[1])

    return R


def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None:
        print('Not Found')
    else:
        print(c)


exec(input().strip())