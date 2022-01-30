mystery_int = 50

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Add some code below that will find and print the sum of
#every odd number between 0 and mystery_int. This time,
#exclude the bounds (e.g. if mystery_int was 51, add the odds
#from 1 to 49, but not 51).
#
#Hint: There are multiple ways to do this!


#Add your code here!

i = 0
total = 0
while i < mystery_int:
    if not i%2 == 0:
        total += i
    i += 1
print(total)

