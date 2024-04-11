def comb_sort(liste):
    len_list = len(liste)
    gap = len_list
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < len_list:
            if liste[i] > liste[i + gap]:
                liste[i], liste[i + gap] = liste[i + gap], liste[i]
                sorted = False
            i += 1

    return liste

ma_liste = [5, 3, 2, 1, 4, 8, 6, 9, 7, 10]
print(comb_sort(ma_liste))