#1.MergeSort
def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):        
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    if left:
        result.extend(left[left_index:])
    if right:
        result.extend(right[right_index:])
    return result
 
def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = MergeSort(left)
    right = MergeSort(right)
    return list(merge(left, right))

#2.QuikSort
def QuikSort(list):
    if len(list) <= 1 :
        return list
    pivot = list[len(list)//2]
    left = [x for x in list if x < pivot]
    middle = [x for x in list if x == pivot]
    right = [x for x in list if x > pivot]
    return(QuikSort(left) + middle + QuikSort(right))

#3.SelectionSort
def SelectionSort(list):
    lenght= len(list)
    while lenght != 0:
        for i in range(lenght):
            selection = [0]
            for j in range(lenght):
                if selection[0] < list[j] :
                    selection = [list[j]]
                    index= j

            lenght -=1
            list[index] = list[lenght]
            list[lenght]=selection[0] 

            selection = [list[0]]
    return list

#4. BubbleSort
def bulles_sort(liste):
    len_list = len(liste) # Prend la longueur de la liste
    
    
    verif = True # Vérifie si des éléments ont été intervertit
    j = 0 # Compte le nombre d'itération dans la boucle
    while verif:
        verif = False
        j += 1
        for i in range(0, len_list - j):
            if liste[i] > liste[i+1]: # Compare le premier élément avec le second élément
                liste[i], liste[i+1] = liste[i+1], liste[i] # Échanger les éléments
                verif = True # Si un échange est effectué, le tri n'est pas encore terminé

    return liste # renvoie la liste trié


#5.heap_sort
def heap_sort(array):
    def heapify(array, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and array[i] < array[left]:
            largest = left

        if right < n and array[largest] < array[right]:
            largest = right

        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            heapify(array, n, largest)

    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

    return array

#6. insertion sort 
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

#7.comb sort 
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
