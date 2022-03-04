#We've written the function, sort_with_bubbles, below. It takes
#in one list parameter, lst. However, there are two problems in
#our current code:
# - There's a missing line
# - There's a semantic error (the code does not raise an
#   error message, but it does not perform correctly)
#
#Find and fix these problems! Note that you should only need
#to change or add code where explicitly indicated.
#
#Hint: If you're stuck, use an example input list and trace
#the code and how it modifies your list on paper. For
#example, try writing out what happens to the following list:
#
#  [34, 16, 2, 78, 4, 6, 1]

def sort_with_bubbles(lst):
    # set swap_occurred to True to guarantee the loop run once.
    swap_occurred = True

    # Run the loop as long as the swap occurred previous time.
    while swap_occurred:
        # start off assuming a swap 
        swap_occurred = False
        for i in range(len(lst) - 1):
            # current, nxt = lst[i], lst[i + 1]
            if lst[i] > lst[i + 1]:
                tmp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = tmp

                swap_occurred = True
    return lst

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: [1, 2, 3, 4, 5]
print(sort_with_bubbles([5, 3, 1, 2, 4]))


