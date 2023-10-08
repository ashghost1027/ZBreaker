def selection_sort(array):

    count = 0
    overcount = 0
    for i in range(len(array)):
        overcount += 1
        for j in range(len(array)):
            count+= 1
            if array[i] < array[j]:
                array[i],array[j] = array[j],array[i]
        
    return [array, overcount, count]

print(selection_sort([1,2,3,4,5,6,7,8,9]))

def bubble_sort(array):
        
        i = 0
        count = 0
        while i+1 < len(array):
            for j in range(len(array)-1):
                count += 1
                if array[j] > array[j+1]:
                    array[j+1], array[j] = array[j], array[j+1]
            i+=1

        return [array, i, count]

print(bubble_sort([2,1,4,5,3,6,74,7,0]))

def insertion_sort(array):
    count = 0
    overcount = 0
    for i in range(1,len(array)):
        count += 1
        for j in range(i):
            overcount += 1
            if array[i] < array[j]:
                array[i],array[j] = array[j], array[i]
    return [array, count, overcount]

print(insertion_sort([4,2,5,8,3,1,9,7]))

def merge_sort(array):
    if len(array)<2:
        return array
    subarray1 = array[:len(array)//2]
    subarray2 = array[len(array)//2:]

    return merge(merge_sort(subarray1),merge_sort(subarray2))

def merge(array1, array2):

    merged_array = []
    while array1 and array2:
        if array1[0] < array2[0]:
            merged_array.append(array1.pop(0))
        else : merged_array.append(array2.pop(0))
    while array1:
        merged_array.append(array1.pop(0))
    while array2:
        merged_array.append(array2.pop(0))
    return merged_array
    

print(merge_sort([9,2,4,6,1,7,8,5,3]))

def quick_sort(array, high, low):
    
    if len(array) < 2:
        return array
    if len(array) == 2:
        if array[0] < array[1]:
            return array
        else :
            array[0], array[1] = array[1], array[0]
            return array
    else:

        pivot = array[high]
        pivot_position = low - 1

        for i in range(low,high):
            if array[i] < pivot:
                pivot_position += 1
                array[i], array[pivot_position] = array[pivot_position], array[i]
        array[pivot_position+1], array[high] = array[high], array[pivot_position+1]   

        return quick_sort(array[:pivot_position+1],pivot_position, 0) + quick_sort(array[pivot_position+1:], len(array[pivot_position+1:])-1, 0)
    
print(quick_sort([2,4,5,7,8,9,3,1], 7, 0))






    