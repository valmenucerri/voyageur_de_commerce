import math as m
import matplotlib.pyplot as plt
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

def lier_points(pt1,pt2):
    plt.plot([pt1[0],pt2[0]],[pt1[1],pt2[1]],linestyle='solid',color='red')

def plus_petite_dist(pt,coord):
    distances = []
    for i in range(len(coord)):
        dist = calcul_distance(pt, coord[i])
        if dist == 0:
            distances.append(999999)
        else:
            distances.append(dist)
    plus_petite = min(distances)
    pt_proche = distances.index(plus_petite)
    return pt_proche

def algo(coord):
    pt_a_etudier = coord[0]
    '''for i in range(len(coord)):
        pt2 = plus_petite_dist(coord[i],coord)
        lier_points(coord[i],coord[pt2])
        coord[i] = coord[pt2]
        '''
    for j in range(len(coord)):
        pt2 = plus_petite_dist(pt_a_etudier, coord)
        lier_points(pt_a_etudier, coord[pt2])
        remplace = coord.index(pt_a_etudier)
        coord[remplace] = [0,0]
        print(coord)
        pt_a_etudier= coord[pt2]




    plt.show()