A function is a reusable block of code or programming statements designed to perform a certain task.
To define or declare a function, Python provides the def keyword. The following is the syntax for defining a function. 
The function block of code is executed only if the function is called or invoked.

Declaring and Calling a Function:

When we make a function, we call it declaring a function. 
When we start using the it, we call it calling or invoking a function. Functions can be declared with or without parameters.
    


# syntax
# Declaring a function
def function_name():
    codes
    codes
# Calling a function
function_name()


Function without Parameters
Function can be declared without parameters.



def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()



Function Returning a Value - Part 1

Functions return values using the return statement. If a function has no return statement, it returns None. 
Let us rewrite the above functions using return. 
From now on, we get a value from a function when we call the function and print it.

def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())



Function with Parameters
In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set) as parameters.

Single Parameter: If our function takes a parameter we should call our function with an argument
    

  # syntax
  # Declaring a function
  def function_name(parameter):
    codes
    codes
  # Calling function
  print(function_name(argument))

#EX
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050




# 2 parameters

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age 

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))




Passing Arguments with Key and Value
If we pass the arguments with key and value, the order of the arguments does not matter.


# syntax
# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
print(function_name(para1 = 'John', para2 = 'Doe')) # the order of arguments does not matter here



def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh')

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter 



Function Returning a Value - Part 2
If we do not return a value with a function, then our function is returning None by default. 
To return a value with a function we use the keyword return followed by the variable we are returning. 
We can return any kind of data types from a function.

def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')




def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2019, 1819))



def is_even (n):
    if n % 2 == 0:
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False


def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))






Function with Default Parameters
Sometimes we pass default values to parameters, when we invoke the function. 
If we do not pass arguments when calling the function, their default values will be used.



def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age 
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon




Arbitrary Number of Arguments
If we do not know the number of arguments we pass to our function,
we can create a function which can take arbitrary number of arguments by adding * before the parameter name.


def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10



def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i) 
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')





Dictionary unpacking
You can call a function which has named arguments using a dictionary with matching key names. You do so using **.

# Define a function that takes two arguments: 'name' and 'location'
def greet(name, location):
    # Print a greeting message using the provided arguments
    print("Hi there", name, "how is the weather in", location)

# Call the function using keyword arguments
greet(name="Alice", location="New York")  
# Output: Hi there Alice how is the weather in New York

# Create a dictionary with keys matching the function's parameter names
my_dict = {"name": "Alice", "location": "New York"}

# Call the function using dictionary unpacking
greet(**my_dict) 





Arbitrary Number of Named Arguments
You can also define a function to accept an arbitrary number of named arguments.

def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(" * key:", k, "value:", v)




Function as a Parameter of Another Function
#You can pass functions around as parameters
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27


def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print('This is the conversion of 100 degrees celsius to Fahrenheit:,', convert_celsius_to_fahrenheit(100), 'F')




def add_all_nums(*nums):
    total = 0
    for num in nums:
        if not isinstance(num, (int, float)):
            return "Error: all arguments must be numbers"
        total += num
    return total

add_all_nums(1, 2, 3)        # returns 6
add_all_nums(5, 2.5, 1.5)    # returns 9.0
add_all_nums(1, "two", 3)    # returns "Error: all arguments must be numbers"




def check_season(month):
    month = month.lower()
    
    if month in ['december', 'january', 'february']:
        return "Winter"
    elif month in ['march', 'april', 'may']:
        return "Spring"
    elif month in ['june', 'july', 'august']:
        return "Summer"
    elif month in ['september', 'october', 'november']:
        return "Autumn"
    else:
        return "Invalid month"
    

    check_season('january')




def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Undefined slope (division by zero)"
    return (y2 - y1) / (x2 - x1)


calculate_slope(0,1,0,5)





import math

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return "No real solutions"
    
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    return x1, x2


solve_quadratic_eqn(2,5,-3)





def print_list(lst):
    for item in lst:
        print(item)


print_list(['Alan','es','chingon','obviooooooo'])




#Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, 
# calculate_range, calculate_variance, calculate_std (standard deviation).




