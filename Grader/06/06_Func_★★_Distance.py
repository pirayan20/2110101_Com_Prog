import math


def distance1(x1, y1, x2, y2):
    x = [x1, x2, y1, y2]
    for i in range(len(x)):
        x[i] = float(x[i])
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return distance


def distance2(p1, p2):
    x1, y1 = float(p1[0]), float(p1[1])
    x2, y2 = float(p2[0]), float(p2[1])
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return distance


def distance3(c1, c2):
    for i in range(len(c1)):
        c1[i] = float(c1[i])
    for i in range(len(c2)):
        c2[i] = float(c2[i])

    x1, y1, r1 = c1[0], c1[1], c1[2]
    x2, y2, r2 = c2[0], c2[1], c2[2]
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)

    if distance <= r1 + r2:
        overlap = True
    else:
        overlap = False

    return distance, overlap


def perimeter(points):
    i = 0
    alldist = []
    while i != len(points)-1:
        dx = int(points[i+1][0]) - int(points[i][0])
        dy = int(points[i+1][1]) - int(points[i][1])
        distance = math.sqrt((dx**2)+(dy**2))
        alldist.append(distance)
        i += 1

    dx = int(points[i][0]) - int(points[0][0])
    dy = int(points[i][1]) - int(points[0][1])
    distance = math.sqrt((dx**2)+(dy**2))
    alldist.append(distance)
    z = sum(alldist)
    return z


exec(input().strip())
