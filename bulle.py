def tri_bulle(tableau):
    permutation = True
    passage = 0
    # Continue tant qu'il y a des permutations à faire
    while permutation == True:
        permutation = False  # Initialise la variable de permutation à False
        passage = passage + 1  # Incrémente le nombre de passages
        # Parcourt le tableau jusqu'à len(tableau) - passage
        for en_cours in range(0, len(tableau) - passage):
            # Vérifie si l'élément actuel est plus grand que le suivant
            if tableau[en_cours] > tableau[en_cours + 1]:
                permutation = True  # S'il y a eu une permutation, met à jour la variable
                # Échange les deux éléments
                tableau[en_cours], tableau[en_cours + 1] = \
                tableau[en_cours + 1],tableau[en_cours]
    return tableau  # Retourne le tableau trié

# Exemple d'utilisation
liste_a_trier = [3, 7, 2, 1, 9, 5]
print("Avant le tri :", liste_a_trier)
liste_triee = tri_bulle(liste_a_trier)
print("Après le tri :", liste_triee)
