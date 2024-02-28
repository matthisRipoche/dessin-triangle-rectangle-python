nbLigne = input("Saisissez un nombre de lignes :")
nbLigne = int(nbLigne)

for i in range(1 ,nbLigne + 1): #parcours chaque ligne

    ligne = "" #initialise la ligne a rien

    if i == nbLigne:
        for j in range(1, i + 1):
            ligne += "#"
    else:
        for j in range(1, i + 1):
            if j == 1 or j == i:
                ligne += "#"
            else:
                ligne += " "
    print(ligne)





        