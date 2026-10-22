def bubble_sort (input_list: list) -> list:

    for j in range(len(input_list) - 1):
        swapped = False
        for i in range(len(input_list) - 1 - j):
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                swapped = True
        if not swapped:
            break
    return input_list
print(bubble_sort([0, 100, 99, 98, 97, 96, 95]))
