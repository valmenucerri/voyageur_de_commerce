'''
Créer un fichier .net qui contient des données aléatoires
'''

import random as r

N = 10  # A changer comme désiré


with open('exemple_graphe/exemple{}.net'.format(N), 'w') as t:
    t.write(str(N) + '\n')
    liste_ligne = []
    for a in range(N-1):
        for b in range(int(r.randint(1, N - 1) /(3/2))):
            j = str(r.randint(a+1, N - 1))
            h = str(r.randint(0, N**2))
            if [j, str(a)] not in liste_ligne:
                t.write(str(a) + " " + j + " " + h +"\n")
                liste_ligne.append([j, str(a)])
