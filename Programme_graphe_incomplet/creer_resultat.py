def resul(parcours,cout,N):
    with open("Résultats/exemple{}parcours.txt".format(N),'w') as fichier:
        for i in parcours:
            fichier.write(i)
        fichier.write("\n"+ "Le coût total du voyage est :"+ str(cout))

