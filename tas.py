def tri_par_tas(tableau):
    def entasser(tableau, n, i):
        plus_grand = i
        gauche = 2 * i + 1
        droite = 2 * i + 2

        if gauche < n and tableau[i] < tableau[gauche]:
            plus_grand = gauche

        if droite < n and tableau[plus_grand] < tableau[droite]:
            plus_grand = droite

        if plus_grand != i:
            tableau[i], tableau[plus_grand] = tableau[plus_grand], tableau[i]
            entasser(tableau, n, plus_grand)

    n = len(tableau)

    for i in range(n // 2 - 1, -1, -1):
        entasser(tableau, n, i)

    for i in range(n - 1, 0, -1):
        tableau[i], tableau[0] = tableau[0], tableau[i]
        entasser(tableau, i, 0)

    return tableau

# Exemple d'utilisation
liste_a_trier = [3, 7, 2, 1, 9, 5]
print("Avant le tri :", liste_a_trier)
liste_triee = tri_par_tas(liste_a_trier)
print("Après le tri :", liste_triee)
