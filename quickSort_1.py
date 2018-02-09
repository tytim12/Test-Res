def quick_sort(list, left, right):
    if left >= right:
        return list

    key = list[left]
    low = left
    high = right

    while left < right:
        while left < right and list[right] >= key:
            right -= 1 
        list[left] = list[right]
        while left < right and list[left] <=key:
            left += 1
        list[right] = list [left]
    
    list[right] = key
    quick_sort(list, low, left - 1)
    quick_sort(list, left + 1, high)
    return list

array = [9,3,2,1,4,6,7,0,5]
quick_sort(array, 0, len(array) - 1)
print(array)