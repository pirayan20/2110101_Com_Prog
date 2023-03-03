import numpy as np

def toCelsius(f):
     return (f-32)*(5/9)

def BMI( wh ):
    bmi = wh[:,0] / (wh[:,1] / 100)**2
    return bmi

def distanceTo( p, Points ):
    dist = (Points[:,0] - p[0])**2 + (Points[:,1]-p[1])**2
    return np.sqrt(dist)

exec(input().strip())