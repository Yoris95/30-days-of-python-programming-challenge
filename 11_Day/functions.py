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

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
# Solution:
def convert_celsius_to_fahrenheit(c):
    f = 0
    f = (c * 9/5) + 32
    return f
print(convert_celsius_to_fahrenheit(30))
                                        # End.

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# Solution 1:
def check_season(month):
    msg1 = "Autumn"
    msg2 = "Summer"
    msg3 = "Spring"
    msg4 = "Winter"
    msg5 = "Undefined - invalid month"
    msg = ""
    if month == "September" or month == "October" or month == "November":
        msg = msg1
    elif month == "June" or month == "July" or month == "August":
        msg = msg2
    elif month == "March" or month == "April" or month == "May":
        msg = msg3
    elif month == "December" or month == "January" or month == "February":
        msg = msg4
    else:
        msg = msg5
    return msg
print(check_season("December"))
                                    # End.

# Solution 2:
def get_season(month):
    season = {
        'Spring': ['March', 'April', 'May'],
        'Summer': ['June', 'July', 'August'],
        'Autumn': ['September', 'October', 'November'],
        'Winter': ['December', 'January', 'February']
        }
    key = season.keys()
    for k in key:
        if month in season[k]: 
            return k
    return 'invalid month'
 
print(get_season('October'))
                                                            # End.
