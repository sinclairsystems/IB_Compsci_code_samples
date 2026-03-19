


def selection_sort(unsorted_list):
    operation_counter = 0
    unsorted_list_length = len(unsorted_list) #we make loops based on length because we are wanting to keep track and swapping indexes instead of the elements themselves
    
    
    for outer_index in range (unsorted_list_length):
        current_smallest_index = outer_index
        
        for inner_index in range (outer_index + 1, unsorted_list_length):#+1 so we dont compare the same thing
            operation_counter+= 1 #count how many operations we do 
            if unsorted_list[current_smallest_index] > unsorted_list[inner_index]: #this loop just finds the new smallest
                current_smallest_index = inner_index
                
        #once we found the new smallest after a pass we swap items
                
        value_becoming_smallest = unsorted_list[current_smallest_index]
        old_smallest_being_swapped = unsorted_list[outer_index]
            
        unsorted_list[current_smallest_index] = old_smallest_being_swapped
        unsorted_list[outer_index] = value_becoming_smallest
    print(operation_counter)            
    return unsorted_list   
    
small_number_list = [5, 3, 8, 4, 2]

medium_number_list = [42, 17, 93, 58, 21, 7, 64, 39, 81, 12]

reverse_sorted_numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

already_sorted_numbers = [1,2,3,4,5,6,7,8,9,10]

larger_random_numbers = [
67,12,89,34,2,45,78,90,11,56,
43,21,98,54,76,32,87,65,23,9,
100,5,73,28,91,14,60,3,47,88
]

sorted_small_number_list = selection_sort(reverse_sorted_numbers)                
                
print(sorted_small_number_list)            