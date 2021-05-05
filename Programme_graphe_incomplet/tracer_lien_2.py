from copy import deepcopy
import Programme_graphe_incomplet.creer_resultat as cr

def petit_cout(liste,ancien_noeud):
    '''
    Trouver l'indice du noeud pour lequel le trajet est le moins cher, c'est à dire avec la plus petite valeur sur l'arête intermédiaire
    :param liste: le noeud considéré. type : list
    :param ancien_noeud: l'indice du dernier noeud exploré. type : int
    :return: petit_cout: l'indice du noeud suivant, qui est le moins cher à rallier. type : int
    '''
    cout = []
    for i in liste:
        if i[0] != ancien_noeud: #considérer tous les noeuds sauf le dernier parcouru, éviter les retours en arrière
            cout.append(i[1])
        else:
            cout.append(99999) #rajouter une énorme valeur pour ne pas qu'elle soit considérée comme la valeur in
    if cout == []:
        return ancien_noeud #arrêter la fonction, l'indice cherché est l'ancien noeud, car le noeud actuel est une feuille
    petit = min(cout)
    petit_cout = cout.index(petit)
    return petit_cout

def petit_noeud(L,N):
    '''
    Trouver le noeud qui possède le minimum d'arêtes dans le graphe
    :param L: la liste représentant le graphe . type : list
    :param N: la dimension du graphe, son nombre total de noeud. type : int
    :return: petit_noeud: l'indice du noeud ayant le moins d'arête. type : int
    '''
    noeud = [] #créer une liste contenant le nombre d'arête par noeud
    l_neuf = deepcopy(L) #copier la liste de liste pour ne pas la modifier
    for i,j in enumerate(l_neuf):
        if j == []:
            l_neuf[i] = [1 for _ in range(N)] #ajouter une liste de taille N, pour éviter que la liste vide sot considérée comme le noeud avec le moins d'arêtes
            noeud.append(N)
        else:
            noeud.append(len(j))
    petit = min(noeud)
    petit_noeud = noeud.index(petit)
    return petit_noeud

def parcourir_graphe(L,N):
    '''
    Déterminer le parcours le mins coûteux pour parcourir tous les noeuds.
    :param L: le graphe. type : list
    :param N: la dimension du graphe, nombre de noeuds. type : int
    :return: None

    '''
    parcours = [] #créer le parcours final
    indice_prec =[] #créer la liste de tous les indices parcourus
    indice  = petit_noeud(L,N)
    indice_prec.append(indice)
    parcours.append(str(indice))
    nbr_noeud = 1 #créer un compteur du nombre de noeusds traités
    cout = 0
    while nbr_noeud != N:
        ancien_noeud = indice_prec[-1]
        noeud = L[indice]
        if noeud == []:   #considérer le noeud précédent si l'actuel n'a pas d'arête autre que la dernière empruntée
            indice = indice_prec[-retour]
            retour += 1  #considérer les noeuds précédents jusqu'à avoir un noeud ayant un arête inexplorée
            if retour >= len(indice_prec):
                indice = petit_noeud(L, N)


        else:
            ind_faible_cout = petit_cout(noeud,ancien_noeud)
            indice_prec.append(indice)
            indice = noeud[ind_faible_cout][0] #trouver l'indice du noeud suivant, déterminer grâce à ind_faible_cout
            if str(indice) not in parcours:
                cout += noeud[ind_faible_cout][1]
                nbr_noeud += 1 #rajouter 1 au compteur de noeud, car un nouveau noeud non-exploré est ajouté au parcours
                parcours.append('-> ')
                parcours.append(str(indice))

            else:
                parcours.append('<->')
                parcours.append(str(indice))
            del L[indice_prec[-1]][ind_faible_cout]
            retour = 1


    validite = verifier_passage(parcours,N) #vérifier une dernière fois que tous les noeuds ont été parcourus
    cr.resul(parcours,cout,N,validite)


def verifier_passage(parcours,N):
    '''
    Vérifier que tous les noeuds du graphe ont été parcourus à la fin du parcours.
    :param parcours: le parcours final. type : list
    :param N: la dimension du graphe. type : int
    :return: True si tous les noeuds ont été parcourus, False sinon. type : bool
    '''
    valide = 0
    for _ in range(N):
        if str(_) in parcours:
            valide += 1

    if valide == N:
        return True
    else:
        return False