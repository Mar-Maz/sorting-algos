def selection_sort(input_list):
    for i in range(len(input_list) - 1):
        min = 999999999999
        for j in range(i, len(input_list)):
            if input_list[j] < min:
                min = input_list[j]
                min_ind = j

        input_list[i], input_list[min_ind] = input_list[min_ind], input_list[i]
    return input_list

print(selection_sort([100, 94, 88, 82, 76]))