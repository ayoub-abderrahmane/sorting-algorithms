def insertion_sort(liste):
    len_list = len(liste)
    for i in range(len_list):
        key = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > key:
            liste[j + 1] = liste[j]
            j -= 1
            liste[j + 1] = key
    return liste

ma_liste = [5, 3, 2, 1, 4, 9, 6, 8, 10, 7]
insertion_sort(ma_liste)