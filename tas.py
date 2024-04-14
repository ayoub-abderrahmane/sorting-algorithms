def tri_par_tas(tableau):
    # Définition d'une fonction locale pour entasser les éléments dans le tas
    def entasser(tableau, n, i):
        plus_grand = i
        gauche = 2 * i + 1
        droite = 2 * i + 2

        # Vérifie si le fils gauche existe et s'il est plus grand que le parent
        if gauche < n and tableau[i] < tableau[gauche]:
            plus_grand = gauche

        # Vérifie si le fils droit existe et s'il est plus grand que le parent ou le fils gauche
        if droite < n and tableau[plus_grand] < tableau[droite]:
            plus_grand = droite

        # Si le plus grand élément n'est pas le parent, échange les éléments et réapplique l'entassement
        if plus_grand != i:
            tableau[i], tableau[plus_grand] = tableau[plus_grand], tableau[i]
            entasser(tableau, n, plus_grand)

    # Nombre d'éléments dans le tableau
    n = len(tableau)

    # Construction du tas (heap) en partant des feuilles jusqu'à la racine
    for i in range(n // 2 - 1, -1, -1):
        entasser(tableau, n, i)

    # Extraction des éléments du tas un par un pour obtenir le tableau trié
    for i in range(n - 1, 0, -1):
        # Échange le premier élément (le plus grand) avec le dernier élément
        tableau[i], tableau[0] = tableau[0], tableau[i]
        # Réduit la taille du tas et réapplique l'entassement pour maintenir la propriété du tas
        entasser(tableau, i, 0)

    # Retourne le tableau trié
    return tableau

# Exemple d'utilisation
liste_a_trier = [3, 7, 2, 1, 9, 5]
print("Avant le tri :", liste_a_trier)
liste_triee = tri_par_tas(liste_a_trier)
print("Après le tri :", liste_triee)
