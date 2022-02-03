#Write a function called lucky_sevens that takes in one
#parameter, a string variable named a_string. Your function
#should return True if there are exactly three '7's in
#a_string. If there are less than three or more than three
#'7's, the function should return False.
#
#For example:
#  - lucky_sevens("happy777bday") should return True.
#  - lucky_sevens("h7app7ybd7ay") should also return True.
#  - lucky_sevens("happy77bday") should return False.
#  - lucky_sevens("h777appy777bday") should also return False.
#
#Hint: Remember in Chapter 3.3, we covered how to use a loop
#to look at each character in a string.


#Write your function here!

def lucky_sevens(a_string):  # function to return true if exactly 3 sevens

   counter = 0  # counts the number of times 7 occurs in the a_string

   for i in a_string:  # loops through the a_string

       if i == "7":  # if 7 occurs in the a_string

           counter = counter + 1  #counter increases by 1 every time 7 occurs

   if counter == 3:  #if 7 occurs exactly 3 times in a_string

       return True  #returns true

   else:  # 7 occurs less or more than 3 times in a_string

       return False  # returns false

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, True, False, False, each on their own line.
print(lucky_sevens("happy777bday"))
print(lucky_sevens("h7app7ybd7ay"))
print(lucky_sevens("happy77bday"))
print(lucky_sevens("h777appy777bday"))




