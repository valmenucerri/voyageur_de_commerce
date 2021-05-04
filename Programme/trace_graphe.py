import random as rd
import matplotlib.pyplot as plt


def creer_pt(n):
    '''
    Créer un nuage de points générés aléatoirement, et les tracer sur un graphe
    :param n: le nombre de points désiré. type : int
    :return: x,y : les coordonnées en abscisse et en ordonnée de chaque point. type : list
    '''
    x = [ rd.random() for _ in range(n) ]
    y = [ rd.random() for _ in range(n) ]
    plt.scatter(x, y)
    return x,y




