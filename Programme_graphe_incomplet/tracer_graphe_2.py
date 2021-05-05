import Programme.lier_points as lp
import matplotlib.pyplot as plt
import random as r

def trouver_milieu(pt1,pt2):
    x_mil = (pt1[0]+pt2[0]) / 2
    y_mil = (pt1[1]+pt2[1]) / 2
    milieu = [x_mil,y_mil]
    return milieu

def tracer_graphe(L,N):
    x = [r.randrange(0,N*2,2) for i in range(N)]
    y = [r.randrange(0,N*2,2) for y in range(N)]
    coordonnees = lp.coord_pt(x,y)
    plt.xlim(-3,N*2+3)
    plt.ylim(-3,N*2+3)
    for pt in range (N):
        plt.scatter(x[pt],y[pt],s=N*5)
        plt.text(x[pt]-(3/N),y[pt]-(3/N),str(pt))

    plt.show()