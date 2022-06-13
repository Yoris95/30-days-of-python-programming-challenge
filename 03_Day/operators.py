#30 Days Of Python: Day 3 - Operators

age = 27
height = 70.2
j=2
x=5
my_number = 2 + j + x

a = int(input('Input your base number: ', ))
h = int(input('Input your height number: ', ))
area_of_triangle = 0.5 * a * h
print('The area of the triangle is', area_of_triangle)

a = int(input('Input your side a number: ', ))
b = int(input('Input your side b number: ', ))
c = int(input('Input your side c number: ', ))
perimeter_of_triangle = a + b + c
print('The perimeter of the triangle is', perimeter_of_triangle)

l = 5
w = 6
area_of_rectangle = l * w
perimeter_of_rectangle = 2 * (l + w)
print('The area of the rectangle is', area_of_rectangle)
print('The perimeter of the rectangle is', perimeter_of_rectangle)

r = 6
pi = 3.14
area_of_circle = pi * r * r
circumference_of_circle = 2 * pi * r
print('The area of circle is', area_of_circle)
print('The circumference of circle is', circumference_of_circle)

x = int(input('Enter your number:', ))
y = (2*x) - 2
print('y is', y)

x1 = 2
y1 = 2
x2 = 6
y2 = 10
m = (y1-y2) / (x2-x1)
print('the slope m is', m) 

d = y is m 
print(d)
e = m == y
print(e)
f = m != y
print(f)

x = int(input('input x: ', ))
y = (x**2) + (6*x) + 9
print('y is ', y)

print(len('python'))
print(len('dragon'))
print('python' == 'dragon')

print('jargon' in 'I hope this course is not full of jargon')
print('on' in 'dragon and python') 

d = float(len('python'))
print(d)
r = str(d)
print(type(r))
