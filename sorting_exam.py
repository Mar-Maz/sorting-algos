def bubble_sort(arr):
    for i in range(len(arr) - 1):
        swaped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                swaped = True
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
        if not swaped:
            return arr
    return arr
print('сортировка пузырьком')
print(bubble_sort([1, 2, 3, 4, 5]))
print(bubble_sort([5, 4, 3, 2, 1]))
print(bubble_sort([1, 3, 2, 4, 5]))
print(bubble_sort([]))
print(bubble_sort([5]))

###############################################

def selection_sort(arr):

    for i in range(len(arr) - 1):
        min = arr[i]
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < min:
                min = arr[j]
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


print('\nсортировка выборкой')
print(selection_sort([1, 2, 3, 4, 5]))
print(selection_sort([5, 4, 3, 2, 1]))
print(selection_sort([1, 3, 2, 4, 5]))
print(selection_sort([]))
print(selection_sort([5]))

################################################

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        for j in range(i - 1, -1, -1):
            if arr[j] > key:
                arr[j + 1] = arr[j]
                if j == 0:
                    arr[j] = key
                    break
            else:
                arr[j + 1] = key
                break
    return arr

print('\nсортировка вставкой')
print(insertion_sort([1, 2, 3, 4, 5]))
print(insertion_sort([5, 4, 3, 2, 1]))
print(insertion_sort([1, 3, 2, 4, 5]))
print(insertion_sort([]))
print(insertion_sort([5]))


################################################

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    lefthalf = merge_sort(arr[:mid])
    righthalf = merge_sort(arr[mid:])

    return merge(lefthalf, righthalf)

def merge(left, right):
    i = j = 0
    sorted_list = []

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            sorted_list.append(right[j])
            j += 1
        else:
            sorted_list.append((left[i]))
            i += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

print('\nсортировка слиянием')
print(merge_sort([1, 2, 3, 4, 5]))
print(merge_sort([5, 4, 3, 2, 1]))
print(merge_sort([1, 3, 2, 4, 5]))
print(merge_sort([]))
print(merge_sort([5]))

###################################################

def quick_sort(arr, l, h):
    if l >= h:
        return
    pivot_index = partition(arr, l, h)
    quick_sort(arr, l, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, h)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1]
arr3 = [1, 6, 2, 5, 4, 3]

quick_sort(arr1, 0, 4)
quick_sort(arr2, 0, 4)
quick_sort(arr3, 0, 5)

print('\nбыстрая сортировка')
print(arr1, arr2,  arr3, sep='\n')

