def bulles_sort(liste):
    len_list = len(liste) # Prendre la longueur de la liste
    
    
    verif = True
    j = 0
    while verif:
        verif = False
        j += 1
        for i in range(0, len_list - j):
            if liste[i] > liste[i+1]: # Compare le premier élément avec le second élément
                liste[i], liste[i+1] = liste[i+1], liste[i] # Échanger les éléments
                verif = True # Si un échange est effectué, le tri n'est pas encore terminé

    return liste # renvoie la liste trié

resultat = bulles_sort([5,3,2,1,4,9,6,10,8,7])
print(resultat)