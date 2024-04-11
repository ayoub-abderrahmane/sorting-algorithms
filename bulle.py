def tri_bulle(tableau):
    permutation = True
    passage = 0
    while permutation == True:
        permutation = False
        passage = passage + 1
        for en_cours in range(0, len(tableau) - passage):
            if tableau[en_cours] > tableau[en_cours + 1]:
                permutation = True
                # On échange les deux éléments
                tableau[en_cours], tableau[en_cours + 1] = \
                tableau[en_cours + 1],tableau[en_cours]
    return tableau

# Exemple d'utilisation
liste_a_trier = [3, 7, 2, 1, 9, 5]
print("Avant le tri :", liste_a_trier)
liste_triee = tri_bulle(liste_a_trier)
print("Après le tri :", liste_triee)
