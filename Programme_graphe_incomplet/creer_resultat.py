def resul(parcours,cout,N,validite):
    '''
    Créer le fichier résultat, contenant le parcours et le coût total de l'exécution de celui-ci
    :param parcours: le parcours final. type : list
    :param cout: le coût nécessaier pour tout parcourir. type : int
    :param N: la dimension du graphe. type : int
    :param validite: True si tous les noeuds ont été parcoursus, False sinon. type : bool
    :return: None
    '''
    with open("Résultats/exemple{}parcours.txt".format(N),'w') as fichier:
        for i in parcours:
            fichier.write(i)
        fichier.write("\n"+ "Le coût total du voyage est :"+ str(cout))

        if validite:
            fichier.write("\n"+"Tous les noeuds ont été parcourus")
        else:
            fichier.write("\n"+"il manque quelques noeuds")