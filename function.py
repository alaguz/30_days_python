print(10) # Print is a function
print('Alan is a beast')
print(11.0)
print(10 + 10j) #Comlex data type


aa = 'alan'
len(aa)

mats = -10
abs(mats)

type(mats)
type(aa)


str(mats)

num = 20
num = float(num)
print(num)


help('keywords') # Gives a list of Python key words # also built in Python FUnctions

help(str)
dir(str)

help('keywords')

min(0.5,0.1,5.9,6.8)
max(3,45,333333,21,3434,434343243434)
min([1,2,3,4,5,])
max([56,3,34,22,12])

sum([1,2,3,4,5])





🧠 Big Picture
✅ Types that SUPPORT indexing/slicing:
str (strings)
list
tuple
⚠️ Partial (no indexing, but access exists):
dict (uses keys, not indexes)
❌ Do NOT support indexing:
set
int
float
bool

# Indexing and Slicing



numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])  
# Output: [5, 4, 3, 2, 1]


text = "hello"

print(text[0])   # 'h'
print(text[-1])  # 'o'

Slicing:

print(text[1:4])   # 'ell'
print(text[:3])    # 'hel'
print(text[::2])   # 'h


#Lists

nums = [10, 20, 30, 40]

print(nums[0])   # 10
print(nums[-1])  # 40

Slicing:
print(nums[1:3])   # [20, 30]
print(nums[:2])    # [10, 20]
print(nums[::-1])  # reversed


# Tuples


t = (10, 20, 30)

print(t[1])      # 20 #Indexing
print(t[0:2])    # (10, 20) #Slicing

#Dictionary
person = {"name": "Alice", "age": 25}

print(person["name"])   # Alice -- similar to indexing, but you use the key instead



##########################################

# Sets

s = {1, 2, 3}

print(s[0])   # ❌ ERROR -- no order so no indexing


# Int, Float, Boolean -- No indexing and slicing -- unordered
x = 123
print(x[0])   # ❌ ERROR


🧠 Mental model
Strings, lists, tuples → “ordered sequences” → indexable
Dict → “labeled data” → use keys
Set → “unique unordered” → no indexing
Numbers/bool → single values



asd = 'python'
print(asd[1:-1])


###############################################################################################################

# Variables

Variables store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. 
A mnemonic variable is a variable name that can be easily remembered and associated. 
A variable refers to a memory address in which data is stored. 
Number at the beginning, special character, hyphen are not allowed when naming a variable. 

A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) 
is highly recommended.


Python Variable Name Rules

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)



# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
is_graduated = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }


first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True


# variables with the input()

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)


# Casting:

Converting one data type to another data type. We use int(), float(), str(), list, set 
When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error.
If we concatenate a number with a string, the number should be first converted to a string. 
We will talk about concatenation in String section.


# int to float

num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0


num_int = float(num_int)
print(num_int)


# Examples
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']




# Practice

# Define numbers
num_one = 10
num_two = 3

# Arithmetic operations
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# Print results
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor Division:", floor_division)


# Circle calculations
radius = 30

pi = 3.14159

area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

print("Area of circle:", area_of_circle)
print("Circumference of circle:", circum_of_circle)

# Take user input for radius
user_radius = float(input("Enter radius: "))

area = pi * user_radius ** 2

print("Area with user radius:", area)











