def recup_fichier(liste):
    '''
    Récupérer le nom du fichier dans la ligne de commande

    :param liste: la liste cotenant les informations de la ligne de commande. type : list

    :return: graphe : le nom du fichier. type : str
    '''
    graphe = str(liste[-1])
    return graphe



def nbr_noeud(graphe):
    '''
    Récupérer le nombre total de noeuds, c'est à dire la dimension du graphe

    :param graphe: le nom du fichier du graphe. type : str
    :return: N : le nombre total de noeuds. type : int
    '''
    with open("exemple_graphe/"+graphe,'r') as fichier:
        N = fichier.readline()
        N = int(N)
    return N

def analyser_graphe(graphe,N):
    '''
    Créer le dictionnaire associé au graphe, de la forme {noeud : {noeud(s) adjacent(s)}}
    :param graphe: le nom du fichier. type : str
    :param N: le nombre total de noeuds. type : int
    :return: L : le dictionnaire associé au graphe. type : dict
    '''
    L = [[] for i in range (N)]
    with open("exemple_graphe/"+graphe,'r') as fichier:
        for ligne in fichier:
            ligne1 = ligne.split()
            if len(ligne1) == 3:  # Traiter chaque valeur sauf la première, qui est N la dimension du graphe
                couple1 = int(ligne1[0])
                couple2 = int(ligne1[1])
                couple3 = int(ligne1[2])
                if 0 <= couple1 <= N and 0 <= couple2 <= N:
                    L[couple1].append((couple2,couple3))
                    L[couple2].append((couple1, couple3)) #Ajouter le lien opposé , si A va vers B, alors B va vers A

            elif len(ligne1) == 0:  # Ne pas considérer les lignes vides
                pass

    return L