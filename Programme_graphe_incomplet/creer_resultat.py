def resul(parcours,cout,N,validite):
    with open("Résultats/exemple{}parcours.txt".format(N),'w') as fichier:
        for i in parcours:
            fichier.write(i)
        fichier.write("\n"+ "Le coût total du voyage est :"+ str(cout))

        if validite:
            fichier.write("\n"+"Tous les noeuds ont été parcourus")
        else:
            fichier.write("\n"+"il manque quelques noeuds")