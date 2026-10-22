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

print(selection_sort([100, 94, 88, 82, 76]))