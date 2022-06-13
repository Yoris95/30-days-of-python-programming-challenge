# Day 2: 30 Days of python programming

# Exercise: Level 1
firts_name = 'Yoris'
last_name = 'Rombe'
full_name = 'Yoris Rombe'
country = 'Indonesia'
city = 'Makassar'
age = 27
year = 2022
is_married = 'No'
is_true = False
is_light_on = True
firts_name, last_name, full_name = 'Yoris', 'Rombe', 'Yoris Rombe'

# Exercise: Level 2
print(type(firts_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type((firts_name, last_name, full_name)))
print(len(firts_name))
print(len(firts_name)/len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(floor_division)

r = 30
area_of_circle = 3.14 * (r)**2
circum_of_circle = 2 * 3.14 * r
print(area_of_circle)
print(circum_of_circle)

print('Enter your number:')
r = input()
r2 = int(r)
area_of_circle = 3.14 * (r2)**2
print(area_of_circle)

first_name = input()
last_name = input()
country = input()
age = input()
print(first_name + ' ' + last_name + ' ' + country + ' ' + age)