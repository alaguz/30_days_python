Tuples
A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

tuple(): to create an empty tuple
count(): to count the number of a specified item in a tuple
index(): to find the index of a specified item in a tuple
+ operator: to join two or more tuples and to create a new tuple




# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()


alan = ()
alann = tuple()
print(alann)

# syntax
tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')

# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl)


# Syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
print(first_item)
second_item = tpl[-3]

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]


# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]


## Changing Tuples to Lists
## We can change tuples to lists and lists to tuples. Tuple is immutable if we want to modify a tuple we should change it to a list.


# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)


fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')


tuup = (1,2,4)
"2" in tuup  #False
2 in tuup  #True


fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables


# delete a tuple
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1
print(tpl1)



#Practice

vegetables = ('corn','tomato','avocado')
fruit = ('apple','orange','kiwi')
meat = ('chicken','fish','lamb')
food_stuff = vegetables+fruit+meat
print(food_stuff)

print(food_stuff[3:6])

print(food_stuff[0:3])

del food_stuff
print(food_stuff)


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(nordic_countries[0])
"Estonia" in nordic_countries
"Iceland" in nordic_countries

