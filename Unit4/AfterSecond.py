#Write a function called after_second that accepts two 
#arguments: a target string to search, and string to search
#for. The  function should return everything in the first
#string *after* the *second* occurrence of the search term.
#You can assume  there will always be at least two
#occurrences of the search term in the first string. 
#
#For example:
#  after_second("11223344554321", "3") -> 44554321
#
#The search term "3" appears at indices 4 and 5. So, this
#returns everything from the index 6 to the end.
#
#  after_second("heyyoheyhi!", "hey") -> hi!
#
#The search term "hey" appears at indices 0 and 5. The
#search term itself is three characters. So, this returns
#everything from the index 8 to the end.
#
#Hint: This may be more complicated than it looks! You'll
#have to look at the length of the search string and
#either modify the target string or take advantage of the
#extra arguments you can pass to find().


#Write your function here!

def after_second(s,sub):#defining a method a fter_second

   first = s.find(sub)#defining a variable first that hold method find value

   if first != -1:#defining if block to check first variable value not equal to -1 using slicing  

       s = s[len(sub)+first:]#defining s variable to calculate sub parameter length of parameter and use slicing

       second = s.find(sub)#defining second variable to calculate find method value  

   if second != -1:#defining if block to calculate second variable slicing

       return s[len(sub)+second:]#return s variable value




#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 44554321 and hi!, each on their own line.
print(after_second("11223344554321", "3"))
print(after_second("heyyoheyhi!", "hey"))



