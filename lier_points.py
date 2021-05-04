import math as m
def coord_pt(x,y):
    coord = []
    for i in range (len(x)):
        coord.append([x[i],y[i]])

    return coord
def calcul_distance(pt1,pt2):
    x = (pt2[0]-pt1[0])**2
    y = (pt2[1]-pt1[1])**2
    dist = m.sqrt(x+y)
    return dist

