# Introduction
# Day 1 - 30DaysOfPython Challenge

print("Hello World!")   # print hello world
print("Alan is the best in the World and will transfer to engineering")

print(2 + 3)   # addition(+)
print(3 - 1)   # subtraction(-)
print(2 * 3)   # multiplication(*)
print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(18 % 4)
print(29 % 3)

print(type([1,2,3,4]))
print(type(10))
print(type(3.14))
print(type('Alan Jimenez Guzman'))


print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String

print(1+3j)
print(type([1, 2, 3]))           # List
print(type({'name': 'Asabeneh'}))  # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set



x = 15 # Int
pie = 3.14 # Float
boool = False # Boolean
boo = True # Boolean
terminal = [1,2,3,4,5] # List
Alan = 'Jimenez Guzman' # String

farfan_1 = (10,20,30,40)# Tuple -- A tuple is a collection of items that is : Ordered (keeps position) , and Immutable (cannot be changed after creation)
print(farfan_1[2]) # or w/o () -- t = 1,2,3
t = (5,) # also a tuple
print(t[0])
#slicing
print(farfan_1[1:3])

# Dictionary
# Sets


z = 9 -10j  # Complex -- The 9 is the real part and the 50j is the imagianary part -- can do math with Complex data types --They’re used in advanced math and engineering
print(z.real)
print(z.imag)


trump = { # Dictionary
    "name":"Donald",
    "AGE": 100
}

print(trump["name"])
print(trump["AGE"])


#or

print(trump.get("name"))
print(trump.get("AGE"))

trump["name"] = "Ivanka"
trump["AGE"] = 70

print(trump)

trump.keys()
trump.values()
trump.items()


# Dictionaries ans Sets have same rules for mutable and inside being immutable -- For Dictionaries the immutable part is the key

#set -- not ordered, no duplicates, mutable    -- 👉 Sets are mutable 👉 But the elements inside a set must be immutable like INT, STRINGS, TUples
#s = {1, 2, 3}           # ints
s = {"a", "b"}          # strings
s = {(1, 2), (3, 4)}    # tuples
n = {1,2,3,4}
print(n)


n.remove(2)
print(n)

n.add(7)
print(n)

a = {1, 2, 3} # Union
b = {3, 4, 5}

print(a | b)

print(a & b) #intersection


nums = {1, 2, 3} # With large data , check if membership exists

print(2 in nums)   # True
print(5 in nums)   # False


s = set() # Empty set
print(s)

