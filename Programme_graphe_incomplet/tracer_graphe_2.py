import Programme.lier_points as lp
import matplotlib.pyplot as plt
import random as r

def trouver_milieu(pt1,pt2):
    x_mil = (pt1[0]+pt2[0]) / 2
    y_mil = (pt1[1]+pt2[1]) / 2
    milieu = [x_mil,y_mil]
    return milieu

def tracer_graphe(L,N):
    x = [r.randrange(0,N*4,3) for i in range(N)]
    y = [r.randrange(0,N*4,3) for y in range(N)]
    coordonnees = lp.coord_pt(x,y)
    plt.xlim(-3,N*4)
    plt.ylim(-3,N*4)
    for pt in range (N):
        plt.scatter(x[pt],y[pt],s=N*7,color = 'orange')
        plt.text(x[pt]-1,y[pt]-1,str(pt))

    plt.show()