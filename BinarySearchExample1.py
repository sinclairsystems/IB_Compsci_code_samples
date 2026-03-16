
def binarySearch(list_to_search, element_to_find):
    start_element = 0  #start of list
    end_element = len(list_to_search)-1 #last element of list
   
    
    while start_element <= end_element:
        print("loop running")
        halfway_element = (start_element + end_element) // 2
        print("halfway el started as: ",halfway_element)
        
        if element_to_find == list_to_search[halfway_element]:
            print("element found")
            print("start element was: ", list_to_search[start_element],"end was: ", list_to_search[end_element] )
            return halfway_element
        
        elif element_to_find > list_to_search[halfway_element]:
        
            start_element =  halfway_element + 1  #start of list
            
            
        elif element_to_find < list_to_search[halfway_element]:
  
            end_element =  halfway_element-1 #last element of list
            
        else:
            print("something went wrong")
            break
        
        
    return -1
            
            

sorted_list = [i for i in range(67)]

sorted_random_nummies = [5, 11, 14, 20, 27, 31, 39, 46, 52, 58, 63, 71, 84, 90, 103, 117, 126, 138, 145, 159]

print(binarySearch(sorted_random_nummies,117))