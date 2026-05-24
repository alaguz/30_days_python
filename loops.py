Life is full of routines. In programming we also do lots of repetitive tasks. 
In order to handle repetitive task programming languages use loops. 
Python programming language also provides the following types of two loops:

while loop
for loop




# While Loop
We use the reserved word while to make a while loop. 
It is used to execute a block of statements repeatedly until a given condition is satisfied. 
When the condition becomes false, the lines of code after the loop will be continued to be executed.


#EX
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4


count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(f"{count} is not greater than 5")



# Break and Continue - Part 1
Break: We use break when we like to get out of or stop the loop.
# syntax


count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break


count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1


# FOR LOOPS

##For Loop
A for keyword is used to make a for loop, similar with other programming languages, but with some syntax differences. 
Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
    


# List

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5


# String

language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])



or 

for char in language:      # Better for Strings
    print(char)



# tuple

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)


# Dict

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out






# sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)


## Short reminder: Break: We use break when we want to stop our loop before it is completed.

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break




## Continue: We use continue when we want to skip some of the steps in the iteration of the loop.

numbers = (0,1,2,3,4,5)

for number in numbers:
    print(number)
    
    if number == 3:
        continue

    if number != 5:
        print('Next number should be', number + 1)
    else:
        print("loop's end")

print('outside the loop')


# The Range Function
The range() function is used to return a list of numbers. The range(start, end, step) takes three parameters: starting, ending and increment. 
By default it starts from 0 and the increment is 1. 
The range sequence needs at least 1 argument (end). Creating sequences using range



lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# for backward from start to end 
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]

#EX
for number in range(11):
    print(number)   # prints 0 to 10, not including 11



# Nested For Loops

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)



#or

for skill in person['skills']:
    print(skill)





# For Else
If we want to execute some message when the loop ends, we use else.


for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)   # else statment does print




for number in range(11):
    if number == 5:
        break                 # the for loop end with the break and the else statement does not print
else:
    print('The loop stops at', number)


Pass
In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors. 
Also we can use it as a placeholder, for future statements.

for number in range(6):
    pass



for i in range(5):
    if i == 2:
        pass  # ignore 2 for now
    else:
        print(i)




