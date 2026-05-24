# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
# Division in python gives floating number
print('Division: ', 4 / 2)
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
# gives without the floating number or without the remaining
print('Division without the remainder: ', 7 // 2)
print('Modulus: ', 3 % 2)                           # Gives the remainder
print('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1+1j)
print('Multiplying complex number: ', (1+1j) * (1-1j))

# Declaring the variable at the top first

a = 3  # a is a variable name and 3 is an integer data type
b = 2  # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total)  # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)  #print('This is the sum:',total)


# Calculating area of a circle
radius = 10                                 # radius of a circle
# two * sign means exponent or power
area_of_circle = 3.14 * radius ** 2
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')



# Comparison operators 

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False  , not equal to 
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True , equal
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)



print('True and True: ', True and True)   # Logical operator
print('True or False:', True or False)     # Logical Operator

print(not(1 ==1)) #Logical Operator



In addition to the above comparison operator Python uses:

is: Returns true if both variables are the same object(x is y)
is not: Returns true if both variables are not the same object(x is not y)
in: Returns True if the queried list contains a certain item(x in y)
not in: Returns True if the queried list doesn't have a certain item(x not in y)

# Another way comparison
# True - because the data values are the same
print('1 is 1', 1 is 1)
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh')  # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh')  # False -there is no uppercase B
# True - because coding for all has the word coding
print('coding' in 'coding for all')
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True




aaa = 10
bbb = 10.0
print(aaa is bbb)
print(aaa is not bbb)


ccc = 'apple'
ddd = "the apple tree is greeen and brown with a little of red"
print('verify the word apple in Variable ddd:', ccc in ddd)




#Logical Operators    --  used to combine conditional statements

print(3 > 2 and 4 > 3)  # True - because both statements are true
print(3 > 2 and 4 < 3)  # False - because the second statement is false
print(3 < 2 and 4 < 3)  # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False)  # False -- reverses the result


base = int(input('base:'))
height = int(input('height:'))
print(base)
print(height)
area_of_triangle = base * height * 0.5
print(area_of_triangle)


a = int(input('a:')) 
b = int(input('b:'))
c = int(input('c:'))

print(a)
print(b)
print(c)

perimeter = a + b + c
print(perimeter)



# 1. Rectangle: area and perimeter
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area_rect = length * width
perimeter_rect = 2 * (length + width)
print("Rectangle area:", area_rect)
print("Rectangle perimeter:", perimeter_rect)

# 2. Circle: area and circumference
pi = 3.14
radius = float(input("Enter radius of circle: "))
area_circle = pi * radius * radius   # or pi * radius ** 2
circumference = 2 * pi * radius
print("Circle area:", area_circle)
print("Circle circumference:", circumference)

# 3. Slope, x-intercept, y-intercept of y = 2x - 2
m = 2
b = -2
x_intercept = -b / m
y_intercept = b
print("Slope:", m)
print("x-intercept:", x_intercept)
print("y-intercept:", y_intercept)

# 4. Slope and distance between (2,2) and (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_points = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Slope between points:", slope_points)
print("Distance:", distance)

# 5. Compare slopes
print("Slopes are equal:", m == slope_points)

# 6. y = x^2 + 6x + 9
for x in range(-5, 2):
    y = x**2 + 6*x + 9
    print(f"x={x}, y={y}")
print("y is 0 when x = -3")

# 7. Length comparison
print("len('python'):", len("python"))
print("len('dragon'):", len("dragon"))
print("Falsy comparison:", len("python") != len("dragon"))

# 8. Check 'on' in both
print("'on' in both:", 'on' in "python" and 'on' in "dragon")

# 9. Check 'jargon' in sentence
sentence = "I hope this course is not full of jargon"
print("'jargon' in sentence:", 'jargon' in sentence)

# 10. There is no 'on' in both (False statement check)
print("No 'on' in both:", not ('on' in "python" and 'on' in "dragon"))

# 11. Convert length of 'python'
length_python = len("python")
print("Float:", float(length_python))
print("String:", str(length_python))

# 12. Check even number
num = int(input("Enter a number: "))
print("Is even:", num % 2 == 0)

# 13. Floor division check
print(7 // 3 == int(2.7))

# 14. Type comparison
print(type('10') == type(10))

# 15. int('9.8') == 10 (this will cause error, so handle it)
try:
    print(int('9.8') == 10)
except:
    print("Cannot convert '9.8' to int directly")


# try:
    x = int(input("Enter number: "))
except ValueError:
    print("Not a valid number")
except TypeError:
    print("Wrong type")



🧠 Simple summary:
except: → catches everything (lazy but risky)
except ValueError: → catches specific error (better)
except ... as e: → lets you see the error



# 16. Calculate pay
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
pay = hours * rate
print("Your weekly earning is:", pay)


years = int(input("Enter number of years: "))

# constants
days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60

# calculate seconds
seconds = years * days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute

print("You can live for", seconds, "seconds.")


Write a Python script that displays the following table

1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125


for i in range(1, 6):
    print(i, 1, i, i**2, i**3)



#ex
range(1, 6, 1)   

Means:

start at 1
add 1 each time
stop before 6


# or

range(1, 10, 2) # output -- 1, 3, 5, 7, 9
