# Level 1
# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
# Solution:
def add_two_numbers(a,b):
    print(a * b)
    return
add_two_numbers(2,3)
                            # End.

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
# Solution:
def area_of_circle(r):
    pi = 3.14
    total = pi * r**2
    return total
print(area_of_circle(3))
                            # End.

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
# Solution:
def add_all_nums(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
print(add_all_nums(10, 20, 30, 50))
                                        # End. 

