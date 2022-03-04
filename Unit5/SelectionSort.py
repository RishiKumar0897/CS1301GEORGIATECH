#We've written the function, sort_with_select, below. It takes
#in one list parameter, a_list. Our version of selection sort
#involves finding the minimum value and moving it to an
#earlier spot in the list.
#
#However, some lines of code are blank. Complete these lines
#to complete the selection_sort function. You should only need
#to modify the section marked 'Write your code here!'

def sort_with_select(a_list):
    # for each index in the list
    for i in range(len(a_list)):
        # Assume first that current item is in the correct order ...
        min_index = i

        # for each item from i to the end of the list
        for j in range(i + 1, len(a_list)):
            if a_list[j] < a_list[min_index]:
                min_index = j
        
        min_value = a_list[min_index] # save current minimum value
    
        del a_list[min_index] # delete the minimum value from the current index.
        a_list.insert(i, min_value) # insert the minmum value at its new index.
        
    return a_list
	

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: [1, 2, 3, 4, 5]
print(sort_with_select([5, 3, 1, 2, 4]))


