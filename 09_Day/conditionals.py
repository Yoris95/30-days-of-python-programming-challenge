# Level 1
# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
'''
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
'''

# Solution:
age = int(input())

if age >= 18:
    print("You are old enough to learn to drive.")
elif 17 <= age < 18:
    print("Wait till next year to learn to drive, buddy!")
elif 0 < age < 17:
    print("You need ", 18 - age, "more years to learn to drive")
else:
    print("You are still in your mom's belly")
                                                                    # End.

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
'''
Enter your age: 30
You are 5 years older than me.
'''
# Solution:
my_age = int(input("Enter my age: ")) 
your_age = int(input("Enter your age: "))
year = my_age - your_age 
if my_age > your_age:
    if (year) == 1:
        print("I am 1 year older than you")
    else:
        print("I am", year, "years older than you")
elif your_age > my_age:
    if (year) == -1:
        print("You are 1 year older than me")
    else:
        print("You are", abs(year), "years older than me")
else:
    print("We are bornt in the same year")
                                                                    # End.
        
# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
'''
Enter number one: 4
Enter number two: 3
4 is greater than 3
'''
