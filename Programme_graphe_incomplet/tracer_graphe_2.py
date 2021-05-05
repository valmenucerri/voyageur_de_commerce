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
    Tracer les deux graphes : le premier est celui initial, tel que pr�sent� dans le fichier, et le second est le graphe apr�s parcours, donc les liens inutiles sont retir�s
    :param L: la liste repr�sentant le graphe. type : list
    :param N: la dimension du graphe. type : int
    :param parcours: le parcours � r�aliser. type : list
    :return:
    '''
    x = [r.randrange(0,N*4,3) for i in range(N)]  #cr�er un nuage de points al�atoires repr�sentant chaque noeud, x absisse et y ordonn�e
    y = [r.randrange(0,N*4,3) for y in range(N)]
    coordonnees = lp.coord_pt(x,y) #r�cup�rer la liste compl�te des coordonn�es de chaque point
    plt.subplot(1,2,1) #s�parer le graphe en deux partiesn �crire sur la premier
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

    plt.subplot(1,2,2) #s�parer le graphe en deux parties, �crire sur la seconde
    plt.xlim(-3, N * 4)
    plt.ylim(-3, N * 4)
    for pt in range (N):  #Replacer les m�mes points que sur le premier graphe
        plt.scatter(x[pt],y[pt],s=N*7,color = 'orange')
        plt.text(x[pt]-1,y[pt]-1,str(pt))
    parcours_final = [int(e) for e in parcours if e != '-> ' and e != '<->' ]#garder uniquement les noeuds travers�s, et leur ordre
    for i in range(len(parcours_final)-1): #tracer les liens entre les noeuds parcourus
        lp.lier_points(coordonnees[int(parcours_final[i])], coordonnees[int(parcours_final[i+1])])




    plt.savefig("Graphe/exemple{}figure.pdf".format(len(coordonnees)))


