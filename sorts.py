# -----------------------------------------------------------------------------------#
# Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that
# repeatedly steps through the list, compares adjacent elements and swaps them if they
# are in the wrong order. The pass through the list is repeated until the list is sorted.
def bubbleSort(data_to_sort):
    for i in range(len(data_to_sort) - 1, 0, -1):
        for j in range(i):
            if data_to_sort[j] > data_to_sort[j + 1]:
                temp = data_to_sort[j]
                data_to_sort[j] = data_to_sort[j + 1]
                data_to_sort[j + 1] = temp

        print(f'Iteration: {abs(i - len(data_to_sort))}', data_to_sort)


list_to_sort = [90, 50, 10, 20, 70, 60, 40, 30, 80]
print('Original List: ', list_to_sort)
bubbleSort(list_to_sort)
print('Sorted List: ', list_to_sort)
# Original List:  [90, 50, 10, 20, 70, 60, 40, 30, 80]
# Iteration: 1 [50, 10, 20, 70, 60, 40, 30, 80, 90]
# Iteration: 2 [10, 20, 50, 60, 40, 30, 70, 80, 90]
# Iteration: 3 [10, 20, 50, 40, 30, 60, 70, 80, 90]
# Iteration: 4 [10, 20, 40, 30, 50, 60, 70, 80, 90]
# Iteration: 5 [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Iteration: 6 [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Iteration: 7 [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Iteration: 8 [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Sorted List:  [10, 20, 30, 40, 50, 60, 70, 80, 90]

# -----------------------------------------------------------------------------------#
# Merge sort is an efficient, general-purpose, comparison-based sorting algorithm. Most
# implementations produce a stable sort, which means that the order of equal elements is
# the same in the input and output. Merge sort is a divide and conquer algorithm.
def mergesort(data_to_sort):
    if len(data_to_sort) > 1:
        mid = len(data_to_sort) // 2
        leftarray = data_to_sort[:mid]
        rightarray = data_to_sort[mid:]

        mergesort(leftarray)
        mergesort(rightarray)

        i, j, k = 0, 0, 0

        while i < len(leftarray) and j < len(rightarray):
            if leftarray[i] < rightarray[j]:
                data_to_sort[k] = leftarray[i]
                i += 1
            else:
                data_to_sort[k] = rightarray[j]
                j += 1
            k += 1

        while i < len(leftarray):
            data_to_sort[k] = leftarray[i]
            i += 1
            k += 1

        while j < len(rightarray):
            data_to_sort[k] = rightarray[j]
            j += 1
            k += 1


list_to_sort = [90, 50, 10, 20, 70, 60, 40, 30, 80]
print('Original List: ', list_to_sort)
mergesort(list_to_sort)
print('Sorted List: ', list_to_sort)
# Original List:  [90, 50, 10, 20, 70, 60, 40, 30, 80]
# Sorted List:  [10, 20, 30, 40, 50, 60, 70, 80, 90]


# -----------------------------------------------------------------------------------#
# Quicksort is an efficient sorting algorithm. Developed by British computer scientist Tony
# Hoare in 1959 and published in 1961, it is still a commonly used algorithm for sorting.
# When implemented well, it can be about two or three times faster than its main competitors,
# merge sort and heapsort.
def quickSort(data_to_sort, first, last):
    if first < last:
        pivotindex = partition(data_to_sort, first, last)
        quickSort(data_to_sort, first, pivotindex - 1)
        quickSort(data_to_sort, pivotindex + 1, last)


def partition(values, first, last):
    pivotvalue = values[first]
    lower = first + 1
    upper = last
    done = False
    while not done:
        while lower <= upper and values[lower] <= pivotvalue:
            lower += 1
        while values[upper] >= pivotvalue and upper >= lower:
            upper -= 1
        if upper < lower:
            done = True
        else:
            temp = values[lower]
            values[lower] = values[upper]
            values[upper] = temp
    temp = values[first]
    values[first] = values[upper]
    values[upper] = temp
    return upper

list_to_sort = [90, 50, 10, 20, 70, 60, 40, 30, 80]
print('Original List: ', list_to_sort)
quickSort(list_to_sort, 0, len(list_to_sort) - 1)
print('Sorted List: ', list_to_sort)
# Original List:  [90, 50, 10, 20, 70, 60, 40, 30, 80]
# Sorted List:  [10, 20, 30, 40, 50, 60, 70, 80, 90]
