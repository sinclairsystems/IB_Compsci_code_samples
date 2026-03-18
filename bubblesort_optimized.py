def bubble_sort(list_of_numbers):
    counter = 0
    list_length = len(list_of_numbers)  # total items in list

    for pass_number in range(list_length):  # each pass moves largest value right
        unsorted_length = list_length - pass_number
        last_index = unsorted_length - 1

        for current_index in range(0, last_index):  # compare neighbours
            counter +=1
            if list_of_numbers[current_index] > list_of_numbers[current_index + 1]:  # wrong order

                # swap values (yes there are shorter ways to write this)
                needs_to_move_down = list_of_numbers[current_index + 1]
                needs_to_move_up = list_of_numbers[current_index]
                list_of_numbers[current_index] = needs_to_move_down
                list_of_numbers[current_index + 1] = needs_to_move_up
                

    print("operations: ",counter )
    return list_of_numbers  # return sorted list

small_number_list = [5, 3, 8, 4, 2]

medium_number_list = [42, 17, 93, 58, 21, 7, 64, 39, 81, 12]

reverse_sorted_numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

already_sorted_numbers = [1,2,3,4,5,6,7,8,9,10]

larger_random_numbers = [
67,12,89,34,2,45,78,90,11,56,
43,21,98,54,76,32,87,65,23,9,
100,5,73,28,91,14,60,3,47,88
]

sorted_small_number_list = bubble_sort(small_number_list)

print(sorted_small_number_list)