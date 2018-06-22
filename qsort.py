# coding: utf-8


def quick_sort(array, left, right):  
    if left >= right:  
        return  
    low = left  
    high = right  
    key = array[low]  
    while left < right:  
        while left < right and array[right] > key:  
            right -= 1  
        array[left] = array[right]  
        while left < right and array[left] <= key:  
            left += 1  
        array[right] = array[left]  
    array[right] = key  
    quick_sort(array, low, left - 1)  
    quick_sort(array, left + 1, high)

a = [2, 3, 5, 1, 0]
quick_sort(a, 0, len(a) - 1)
print a
