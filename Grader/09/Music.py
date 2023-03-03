
def m_sum(m, axis):
    if axis == 0:
        ans = []
        for i in range(len(m[0])):
            c = 0
            for j in range(len(m)):
                c += m[j][i]
            ans.append(c)

    else:
        ans = []
        for i in m:
            c = 0
            for j in i:
                c += j
            ans.append(c)
    return ans 

exec(input().strip())