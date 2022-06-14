# Exercise Level 1.
# 1. Iterate 0 to 10 using for loop, do the same using while loop.
# First solution of "For" loop:
k = [0,1,2,3,4,5,6,7,8,9,10]
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
k = [10,9,8,7,6,5,4,3,2,1,0]
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
