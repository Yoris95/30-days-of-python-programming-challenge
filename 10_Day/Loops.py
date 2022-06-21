# Level 1
# 1. Iterate 0 to 10 using for loop, do the same using while loop.
# First solution of "For" loop:
k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in k:
    print(i)                    
                                # End.

# Second solution of "For" loop:
for i in range(11):
    print(i)
                                # End.

# First solution of "While" loop:
number = 0
while number < 11:
    print(number)
    number = number + 1
                                # End.

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
# First solution of "For" loop:
k = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for i in k:
    print(i)
                                # End.

# Second solution of "For" loop:
n = 0
for n in reversed(range(11)):
    print(n) 
                                # End.

# First solution of "While" loop:
n = 11
while n >= 0:
    print(n)
    n = n - 1 
                                # End.

# Second solution of "While" loop:
n = 0
while n <= 10:
    print(10 - n)
    n = n + 1 
                                # End.

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
'''
  #
  ##
  ###
  ####
  #####
  ######
  ######## 
'''
# First solution: 
n = 0
while n < 7:
    print("#" * (n + 1))
    n = n + 1
                                # End.

# Second solution: 
for i in range(0, 7):
    for j in range(0, 1 + i):
        print('#', end = '')
    print()                                
                                # End.

# Third solution:
for i in range (0, 7):
    for j in range (0, 7):
        if j > i:
            print()
            break
        else:
            print("#", end = "")
                                # End.

# Fourth solution:
sum_line = 7
line = 0
sign = 0
while line < sum_line:
    if (sign) >= (line + 1):
        print()
        line = line + 1
        sign = 0
        continue    
    print("*", end="")
    sign = sign + 1
                                # End.

# 4. Use nested loops to create the following:
'''
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
'''

# First solution:
for i in range(0, 8):
    for j in range(8):
        print('#', end = ' ')
    print()
                                # End.

# 5. Print the following pattern:
'''
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
'''

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

# 7. Use for loop to iterate from 0 to 100 and print only even numbers

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers

# Level 2
# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
'''The sum of all numbers is 5050.'''

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
'''The sum of all evens is 2550. And the sum of all odds is 2500.'''

# Level 3
# 1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

# 3. Go to the data folder and use the countries_data.py file.
'''
What are the total number of languages in the data
Find the ten most spoken languages from the data
Find the 10 most populated countries in the world
'''
