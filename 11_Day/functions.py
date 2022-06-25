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
    season1 = "Autumn"
    season2 = "Summer"
    season3 = "Spring"
    season4 = "Winter"
    error = "Wrong Input!"
    season = ""
    if month == "September" or month == "October" or month == "November":
        season = season1
    elif month == "June" or month == "July" or month == "August":
        season = season2
    elif month == "March" or month == "April" or month == "May":
        season = season3
    elif month == "December" or month == "January" or month == "February":
        season = season4
    else:
        season = error
    return season

n = check_season(input("What month is it now: "))
print("This season is", n)
                                    # End.

# Solution 2:
def check_season(month):
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
    return 'Wrong input'
 
n = check_season(input("What month is it now: "))
print("This season is", n)
                                                            # End.
    
# 6. Write a function called calculate_slope which return the slope of a linear equation
# Solution:
def calculate_slope(m,x,b):
    y = 0
    y = m*x + b
    return y
result = calculate_slope(int(input("m = ")), int(input("x = ")), int(input("b = ")))
print("The result of y is {}".format(result))
                                                        # End.

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# Solution:
def solve_quadratic_eqn(a,b,c,x):
    y = 0
    y = a*(x**2) + b*x + c 
    return y
result = solve_quadratic_eqn(int(input("a = ")), int(input(("b = "))), int(input(("c = "))), int(input(("x = "))))
print("The result of y {}".format(result))
                                                        # End.
