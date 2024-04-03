listes = [4, 13, 11, 6, 9, 7 ,10, 12, 1, 5, 15, 3, 8, 14,2]

def QuikSort(list):
    print(list)
    if len(list) <= 1 :
        return list
    pivot = list[len(list)//2]
    left = [x for x in list if x < pivot]
    middle = [x for x in list if x == pivot]
    right = [x for x in list if x > pivot]
    return(QuikSort(left) + middle + QuikSort(right))

print(QuikSort(listes))