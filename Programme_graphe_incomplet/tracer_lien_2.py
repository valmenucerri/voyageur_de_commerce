def petit_cout(liste):
    cout = []
    for i in liste:
        cout.append(i[1])
    petit = min(cout)
    petit_cout = cout.index(petit)
    return petit_cout

def petit_noeud(L):
    noeud = []
    for i in L:
        noeud.append(len(i))
    petit = min(noeud)
    petit_noeud = noeud.index(petit)
    return petit_noeud

def parcourir_graphe(L,N):
    parcours = []
    L_vide = [[] for i in range (N)]
    indice = indice_prec = petit_noeud(L)
    parcours.append('->'+ str(indice))
    while L != L_vide:
        noeud = L[indice]
        if noeud == []:
            indice = indice_prec
        else:
            faible_cout = petit_cout(noeud)
            indice_prec = indice
            indice = noeud[faible_cout][1]
            parcours.append('-> '+ str(indice))
            del noeud[faible_cout]


    return parcours


