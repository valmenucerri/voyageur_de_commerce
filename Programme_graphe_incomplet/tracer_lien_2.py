from copy import deepcopy

def petit_cout(liste,ancien):
    cout = []
    for i in liste:
        if i[0] != ancien:
            cout.append(i[1])
        else:
            cout.append(99999)
    if cout == []:
        return ancien
    petit = min(cout)
    petit_cout = cout.index(petit)
    return petit_cout

def petit_noeud(L,N):
    noeud = []
    l_neuf = deepcopy(L)
    print('l_neuf avant modif :',l_neuf)
    for i,j in enumerate(l_neuf):
        if j == []:
            l_neuf[i] = [1 for _ in range(N)]
            noeud.append(N)
        else:
            noeud.append(len(j))
    petit = min(noeud)
    petit_noeud = noeud.index(petit)
    return petit_noeud

def parcourir_graphe(L,N):
    parcours = []
    indice_prec =[]
    ancien = -1
    indice  = petit_noeud(L,N)
    indice_prec.append(indice)
    parcours.append(str(indice))
    nbr_noeud = 1
    cout = 0
    while nbr_noeud != N:
        ancien = indice_prec[-1]
        noeud = L[indice]
        if noeud == []:
            indice = indice_prec[-retour]
            retour += 1
            if retour >= len(indice_prec):
                indice = petit_noeud(L, N)


        else:
            faible_cout = petit_cout(noeud,ancien)
            indice_prec.append(indice)
            indice = noeud[faible_cout][0]
            if str(indice) not in parcours:
                print("je passe par", indice)
                cout += noeud[faible_cout][1]
                nbr_noeud += 1
                parcours.append('-> ')
                parcours.append(str(indice))

            else:
                parcours.append('<->')
                print("je passe en retour par ",indice)
                parcours.append(str(indice))
            del L[indice_prec[-1]][faible_cout]
            retour = 1



    return parcours,cout


