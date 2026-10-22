def insertion_sort(input_list):
    if len(input_list) < 2:
        return input_list

    for i in range(1, len(input_list)): # i - неотсортированные элементы
        key = input_list[i]
        key_indx = 0
        for j in range(i - 1, -1, -1): # j - отсортированные элементы

            if key >= input_list[j]:
                key_indx = j + 1
                break
            else:
                input_list[j + 1] = input_list[j]
        input_list[key_indx] = key

    return input_list

print(insertion_sort([3, 4, 1, 3, 2]))
print(insertion_sort([1,2,3,4,5]))


print(insertion_sort([5,4,3,2,1]))


def insertion_sort(input_list):
    if len(input_list) < 2:
        return input_list


    for i in range(1, len(input_list)): # i - неотсортированные элементы
        for j in range(i - 1, -1, -1): # j - отсортированные элементы
            if input_list[j + 1] > input_list[j]:
                break
            else:
                input_list[j + 1], input_list[j] = input_list[j], input_list[j + 1]


def bms_insertion_sort(arr): #рабочая реализация
    for i in range(1, len(arr)):
        key = arr[i]

        for j in range(i - 1, -1, -1):
            if key <= arr[j]:
                arr[j + 1] = arr[j]
                if j == 0:
                    arr[j] = key
                    break
            elif key > arr[j]:
                arr[j + 1] = key
                break
    return arr

print(bms_insertion_sort([3, 4, 1, 3, 2]))
print(bms_insertion_sort([1,2,3,4,5]))