listes = [4, 13, 11, 6, 9, 7 ,10, 12, 1, 5, 15, 3, 8, 14,2]

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
 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right)) 

print(merge_sort(listes))
 
