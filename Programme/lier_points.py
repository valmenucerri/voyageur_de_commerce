import math as m
import matplotlib.pyplot as plt
def coord_pt(x,y):
    '''
    Créer une liste de listes, chaque liste interne représentant les coordonnées [x,y] d'un point.
    :param x: les abscisses des points considérés. type : list
    :param y: les ordonnées des points considérés. type : list
    :return: coord : les couples de coordonnées de chaque point. type : list
    '''
    coord = []
    for i in range (len(x)):
        coord.append([x[i],y[i]])
    return coord


def calcul_distance(pt1,pt2):
    '''
    Calculer la distance algébrique entre deux points
    :param pt1: les coordonnées du 1er point considéré. type : list
    :param pt2: les coordonnées du 2ème pt considéré. type : list
    :return: dist: la distance algébrique entre les deux points. type : float
    '''
    x = (pt2[0]-pt1[0])**2
    y = (pt2[1]-pt1[1])**2
    dist = m.sqrt(x+y)
    return dist

def lier_points(pt1,pt2):
    '''
    Tracer la liaison entre deux points particuliers
    :param pt1: les coordonnées du premier point à relier. type : list
    :param pt2: les coordonnées du second point à relier. type : list
    :return: None
    '''
    plt.plot([pt1[0],pt2[0]],[pt1[1],pt2[1]],linestyle='solid',color='red')

def plus_petite_dist(pt,coord):
    '''
    Trouver les coordonnées du point le plus proche d'un point d'interet parmis un nuage de points.
    :param pt: les coordonnées du point dont on veut trouver le plus proche voisin. type : list
    :param coord: l'ensemble des coordonnées de tous les points du nuage. type : list
    :return: pt_proche: l'indice du point le plus proche du point d'interet. type : int
    '''
    distances = []
    for i in range(len(coord)):  #Chercher parmis l'ensemble des points du nuage
        dist = calcul_distance(pt, coord[i])
        if dist == 0:
            distances.append(999999) #Ajouter une distance très grande à la liste, pour éviter de la considérer plusieurs fois
        else:
            distances.append(dist)
    plus_petite = min(distances)
    pt_proche = distances.index(plus_petite)
    return pt_proche

def tracer_liens(coord):
    '''
    Lier les points entre eux, de proche en proche
    :param coord: les coordonnées de l'ensemble des points du nuage. type : list
    :return: None
    '''
    pt_a_etudier = pt_init = coord[0]
    for j in range(len(coord)-1):
        pt2 = plus_petite_dist(pt_a_etudier, coord)
        lier_points(pt_a_etudier, coord[pt2])
        remplace = coord.index(pt_a_etudier)
        coord[remplace] = [-10,-10]
        pt_a_etudier= pt_final = coord[pt2]

    plt.plot([pt_init[0],pt_final[0]],[pt_init[1],pt_final[1]],linestyle='solid',color='green')
    plt.savefig("Résultats/exemple{}.pdf".format(len(coord)))
