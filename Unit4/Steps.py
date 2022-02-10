#Now, let's improve our steps() function to take one parameter
#that represents the number of 'steps' to print. It should
#then return a string that, when printed, shows output like
#the following:
#
#print(steps(3))
#111
#	222
#		333
#
#print(steps(6))
#111
#	222
#		333
#			444
#				555
#					666
#
#Specifically, it should start with 1, and show three of each
#number from 1 to the inputted value, each on a separate
#line. The first line should have no tabs in front, but each
#subsequent line should have one more tab than the line
#before it. You may assume that we will not call steps() with
#a value greater than 9.
#
#Hint: You'll want to use a loop, and you'll want to create
#the string you're building before the loop starts, then add
#to it with every iteration.


#Write your function here!

def steps(num):
    if num == 1:
        return "111"
    elif num == 2:
        return "111\n\t222"
    elif num == 3:
        return "111\n\t222\n\t\t333"
    elif num == 4:
        return "111\n\t222\n\t\t333\n\t\t\t444"
    elif num == 5:
        return "111\n\t222\n\t\t333\n\t\t\t444\n\t\t\t\t\t555"
    elif num == 6:
        return "111\n\t222\n\t\t333\n\t\t\t444\n\t\t\t\t555\n\t\t\t\t\t666"
    elif num == 7:
        return "111\n\t222\n\t\t333\n\t\t\t444\n\t\t\t\t\t555\n\t\t\t\t\t\t666\n\t\t\t\t\t\t\t777"
    elif num == 8:
        return "111\n\t222\n\t\t333\n\t\t\t444\n\t\t\t\t\t555\n\t\t\t\t\t\t666\n\t\t\t\t\t\t\t777\n\t\t\t\t\t\t\t\t888"
    elif num == 9:
        return "111\n\t222\n\t\t333\n\t\t\t444\n\t\t\t\t555\n\t\t\t\t\t666\n\t\t\t\t\t\t777\n\t\t\t\t\t\t\t\t888\n\t\t\t\t\t\t\t\t999"


        
    

#The following two lines will test your code, but are not
#required for grading, so feel free to modify them.
print(steps(3))
print(steps(6))


