listes = [4, 13, 11, 6, 9, 7 ,10, 12, 1, 5, 15, 3, 8, 14,2]
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
    print(list)
    if len(list) <= 1 :
        return list
    pivot = list[len(list)//2]
    left = [x for x in list if x < pivot]
    middle = [x for x in list if x == pivot]
    right = [x for x in list if x > pivot]
    list=(QuikSort(left) + middle + QuikSort(right))
    return list

#3.SelectionSort
def SelectionSort(list):
    print(list)
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

QuikSort(listes)
print(listes)