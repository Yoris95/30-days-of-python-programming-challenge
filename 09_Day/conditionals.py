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
# Solution:
a = int(input("Enter number one:"))
b = int(input("Enter number two:"))

if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "ia smaller than", b)
else:
    print(a, "is equal to", b)
                                        # End.
 
# Level 2
# 1. Write a code which gives grade to students according to theirs scores:
'''
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
'''
# Solution:
name = str(input("What's your name: "))
score = int(input("What's your score: "))

if 80 <= score <= 100:
    print("You get A, congratulations {}!" .format(name))
elif 70 <= score <= 79:
    print("You get B, well done {}!" .format(name))
elif 60 <= score <= 69:
    print("You get C, not bad {}!" .format(name))
elif 50 <= score <= 59:
    print("You get D, Try harder {}!" .format(name))
elif 0 <= score <= 49:
    print("You get F, Unlucky {}!" .format(name))
else:
    print("Error, try again!")
                                                            # End.

# 2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
# Solution:
print("(Months format: January, February, March, April, May, June, July, August, September, October, November, December)")
month = str(input("What month is it now:"))

if month == ("September" and "October" and "November"):
    print("The season is Autumn")
elif month == ("December" and "January" and "February"):
    print("This season is Winter")
elif month == ("March" and "April" and "May"):
    print("This season is Spring")
elif month == ("June" and "July" and "August"):
    print("This season is Summer")
else:
    print("Wrong input!")
                                                            # End.

# 3. The following list contains some fruits:
'''
fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
'''

