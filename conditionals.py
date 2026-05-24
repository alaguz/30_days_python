a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')



a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')




a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed



Nested Conditions
Conditions can be nested


a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')



# We can avoid writing nested condition by using logical operator and.

a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')



user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')




a = 5
if not a < 0:
    print("A is not negative")



name = "James"
if name in ["James", "John"]:
    print("Allowed")


# also not in


a = None
if a is None:
    print("No value")


x = 5
if 1 < x < 10:
    print("Between 1 and 10")


user = "admin"
age = 20

if user == "admin" and 18 <= age < 65:
    print("Full access")


# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
You are old enough to drive. If below 18 give feedback to wait for the missing amount of years
    
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_left = 18 - age
    print(f"You need {years_left} more year(s) to learn to drive.")



#EX
my_age = 25  # you can change this value

your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age
    if diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {diff} years older than me.")

elif your_age < my_age:
    diff = my_age - your_age
    if diff == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {diff} years older than you.")

else:
    print("We are the same age.")



#EX

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is smaller than b")
else:
    print("a is equal to b")



#EX

score = float(input("Enter your score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
elif 0 <= score < 60:
    print("Grade: F")
else:
    print("Invalid score")




month = input("Enter the month: ").strip().capitalize()
print(month)

if month in ["September", "October", "November"]:
    print("Season: Autumn")
elif month in ["December", "January", "February"]:
    print("Season: Winter")
elif month in ["March", "April", "May"]:
    print("Season: Spring")
elif month in ["June", "July", "August"]:
    print("Season: Summer")
else:
    print("Invalid month")





fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter a fruit: ").strip().lower()

if fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(fruit)
    print("Updated list:", fruits)





#EX

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}



if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])


if 'skills' in person:
    print('Python' in person['skills'])




skills = person['skills']

if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
    print('He is a front end developer')

elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print('He is a backend developer')

elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print('He is a fullstack developer')

else:
    print('unknown title')





if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} is married and lives in Finland.")









# Real life code 

users = {
    "alice": {"password": "1234", "role": "admin"},
    "bob": {"password": "abcd", "role": "user"}
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users:
    if users[username]["password"] == password:
        print(f"Welcome {username}!")

        if users[username]["role"] == "admin":
            print("You have full access.")
        else:
            print("You have limited access.")
    else:
        print("Wrong password.")
else:
    print("User not found.")






