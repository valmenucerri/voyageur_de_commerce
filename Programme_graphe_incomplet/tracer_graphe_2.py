import Programme.lier_points as lp
import matplotlib.pyplot as plt
import random as r



def trouver_milieu(pt1,pt2):
    x_mil = (pt1[0]+pt2[0]) / 2
    y_mil = (pt1[1]+pt2[1]) / 2
    milieu = [x_mil,y_mil]
    return milieu

def tracer_graphe(L,N,parcours):
    '''
    Tracer les deux graphes : le premier est celui initial, tel que présenté dans le fichier, et le second est le graphe après parcours, donc les liens inutiles sont retirés
    :param L: la liste représentant le graphe. type : list
    :param N: la dimension du graphe. type : int
    :param parcours: le parcours à réaliser. type : list
    :return:
    '''
    x = [r.randrange(0,N*4,3) for i in range(N)]  #créer un nuage de points aléatoires représentant chaque noeud, x absisse et y ordonnée
    y = [r.randrange(0,N*4,3) for y in range(N)]
    coordonnees = lp.coord_pt(x,y) #récupérer la liste complète des coordonnées de chaque point
    plt.subplot(1,2,1) #séparer le graphe en deux partiesn écrire sur la premier
    plt.xlim(-3,N*4)
    plt.ylim(-3,N*4)
    for pt in range (N):
        plt.scatter(x[pt],y[pt],s=N*7,color = 'orange')
        plt.text(x[pt]-1,y[pt]-1,str(pt))
    for i in range (N):
        for j in L[i]:
            lp.lier_points(coordonnees[i],coordonnees[j[0]])
            milieu = trouver_milieu(coordonnees[i],coordonnees[j[0]])

            plt.text(milieu[0],milieu[1],str(j[1]),color= 'green')

    plt.subplot(1,2,2) #séparer le graphe en deux parties, écrire sur la seconde
    plt.xlim(-3, N * 4)
    plt.ylim(-3, N * 4)
    for pt in range (N):  #Replacer les mêmes points que sur le premier graphe
        plt.scatter(x[pt],y[pt],s=N*7,color = 'orange')
        plt.text(x[pt]-1,y[pt]-1,str(pt))
    parcours_final = [int(e) for e in parcours if e != '-> ' and e != '<->' ]#garder uniquement les noeuds traversés, et leur ordre
    for i in range(len(parcours_final)-1): #tracer les liens entre les noeuds parcourus
        lp.lier_points(coordonnees[int(parcours_final[i])], coordonnees[int(parcours_final[i+1])])




    plt.savefig("Graphe/exemple{}figure.pdf".format(len(coordonnees)))


