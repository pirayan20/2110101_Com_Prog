import math

def update(points,uses,reward):
    for i in uses:
        for j in points:
            if i == j:
                points[i] -= uses[i]
    for k in points:
        points[k] += points[k]*reward/100
        points[k] = math.floor(points[k])
            

    return points

p = {'a1':100,'a2':50,'a3':20}; u = {'a1':10,'a3':5}; update(p,u,10);print(p)