from docx import Document

doc = Document()

doc.add_heading('Software Engineering / Python Interview Prep Roadmap', 0)

content = """
1. Python Fundamentals
Topics: variables, loops, functions, lists, dictionaries, sets, tuples, OOP basics.

2. Object-Oriented Programming (OOP)
Classes, objects, inheritance, self, super(), method overriding.

3. APIs
Use requests library, work with JSON, HTTP methods (GET/POST).

4. Web Scraping
Use requests + BeautifulSoup, parse HTML, extract data.

5. Virtual Environments
Isolate dependencies using venv.

6. Jupyter Notebook
Interactive coding environment, Shift+Enter to run cells.

7. NumPy
Fast numerical arrays, vectorization, matrices.

8. Pandas
Data analysis with DataFrames.

9. Data Structures
Lists, dictionaries, stacks, queues, trees, graphs, heaps.

10. Algorithms
Sorting, binary search, recursion, DFS, BFS, dynamic programming.

11. Time Complexity
O(1), O(log n), O(n), O(n^2).

12. LeetCode
Focus on patterns: two pointers, sliding window, BFS/DFS, DP.

13. Python Libraries
collections, heapq, itertools.

14. SQL
SELECT, JOIN, GROUP BY.

15. System Design
Scalability, caching, APIs, databases.

16. Behavioral Interviews
Communication, teamwork, problem-solving.

17. Projects
Scrapers, APIs, dashboards, automation tools.

Final Advice:
DSA + LeetCode + Real Projects = Best combination.
"""

#Ai




for line in content.split("\n"):
    doc.add_paragraph(line)

doc.save("Python_Interview_Roadmap.docx")

print("Document created successfully!")




---------------------------------------------------------------------------------------------------------------------------------------------------

Data Structures:


A data structure is a way of organizing, storing, and performing operations on data. Operations performed on a data structure include accessing or
updating stored data, 
searching for specific data, inserting new data, and removing data. The following provides a list of basic data structures.


Linear: arrays, linked lists, stacks, queues.

Nonlinear: trees (including binary search trees, heaps, tries), graphs.

Hash-based: hash tables/maps and sets


The selection of data structures used in a program depends on both the type of data being stored and 
the operations the program may need to perform on that data. 


Ex: If a program requires fast insertion of new data, a linked list may be a better choice than an array.


Linked List : A --> B --> C --> 

Array: [1,2,3,4]






Algorithms:

An algorithm is a set of step-by-step instructions for solving a problem or completing a task. 
It tells us exactly what to do and how to get the final result. Computers use algorithms to help them make decisions, process data, or perform actions automatically. 
They can be very simple, like sorting a list of numbers, or very complex, like recommending videos on YouTube.


Input to the algorithm to produce an Output



Input: Every algorithm starts by taking input data, which can take many forms—numbers, text, images, or other types of information.
Processing: The algorithm processes this input using logical rules and mathematical operations, transforming the data to move closer to a solution.
Output: After processing, the algorithm produces an output — an answer, a decision, or some other meaningful result.
Efficiency: A major goal of any algorithm is efficiency — solving problems quickly while using as few resources (like time and memory) as possible.


Importance of Algorithms
Algorithms help us solve problems in a clear and organized way. Instead of guessing or trying random solutions, an algorithm gives us a fixed method to follow, making the task easier and faster. They are essential because they tell computers exactly what steps to take to complete a task. 
Without algorithms, computers wouldn't know how to properly sort data, search for information, or even display a webpage.

Algorithms find quicker, smarter ways to accomplish tasks while using fewer resources like time, memory, and energy. 
As problems become bigger and more complex, algorithms help break them down into manageable steps. Whether guiding self-driving cars or assisting doctors in detecting diseases early, algorithms make complicated things possible.



Finiteness: The algorithm must end after a finite number of steps.




What are the Characteristics of an Algorithm?
Here are the key characteristics of an algorithm:

Clear and Unambiguous: Every step must be precisely defined.
Input: It should have clearly defined input(s).
Output: It should produce at least one expected output.
Finiteness: The algorithm must end after a finite number of steps.
Effectiveness: Each step must be simple enough to be performed exactly and in a finite amount of time.
Feasibility: Performing the steps using available resources should be possible.
Language Independent: An algorithm is a logical process and should not depend on a specific programming language.


-----------------------------------------------------------------------------------------------------------------------------------------------

Big O Notation:

Part 1: What is Big O Notation?
Big O notation is a way to measure how efficient an algorithm is. It answers two questions:

Time complexity: How does runtime grow as input size increases?

Space complexity: How does memory usage grow as input size increases?

Think of it like this: Big O tells you how your code scales when you give it more data.

Why Do We Care?
Two algorithms might both work, but one might take 1 second with 100 items and the other takes 10 minutes. Big O helps us predict which is better before we run it.

The Key Principle
Big O describes the worst-case scenario and focuses on growth rate, not exact time. We ignore constants and smaller terms because we care about what happens with massive inputs.






Example: If an algorithm takes 3n² + 5n + 10 operations, we simplify to O(n²) because:

Drop the constant 3 → n²

Drop smaller terms 5n + 10 → they don't matter when n is huge

Part 2: Common Time Complexities (From Best to Worst)
Here's the hierarchy:

O(1) - Constant: Same time regardless of input size

#EX

nums = [1,2,3]
nums.append(4) #push to the end
print(nums)
nums.pop() # pop from end
print(nums)


nums[0] #look up
nums[1]
nums[2]


#Constant time to search or perform operation

EX: #  hashMaps and for hashSets
hashMap = {}
hashMap["Key"] = 10  #insert

print("Key" in hashMap) #lookup
print(hashMap["Key"]) #lookup

hashMap.pop("Key") #remove









O(log n) - Logarithmic: Doubles input, adds one operation
#ex binary search

nums = [1,2,3,4,5]
target = 6
1,r=0, len(nums) - 1

while 1<=r:
    m=(1+r) // 2
    if target < nums[m]:
        r=m-1
    elif target > nums[m]:
        1=m+1
    else:
        print(m)
        break
        

#Binary search on BST

def search(root,target):
    if not root:
        return False
    if target < root.val:
        return search(root.left,target)
    elif target > root.val:
        return search(root.right,target)
    else:
        return True



#Heap Push and POP

imprt heapq
minHeap = []
heapq.heappush(minHeap,5)
heapq.heappop(minHeap)










O(n) - Linear: Time grows proportionally with input

# ex: 

nums = [1,2,3]
sum(nums)        #sum of an array

for n in nums:   #looping
    print(n)

#ex

nums.insert(1,100)  #insert middle
print(nums)
nums.remove(100)    # remove middle


print(2 in nums)

print(100 in nums)  # search
print(2 in nums)


#Ex

import heapq
heapq.heapify(nums)  #build heap


## sometimes even nested loops can be 0(n)
## (e.g. monotonic stack or sliding window)






O(n log n) - Linearithmic: Efficient sorting algorithms









O(n²) - Quadratic: Nested loops

#Ex --> if you want to loop through a 2 dimentional array, first go through every row and go through every position in that row

so the outer loop will go through every row and inner loop will go through every position in that row 

nums = [[1,2,3], [4,5,6], [7,8,9]]

for i in range(len(nums)):
    for j in range(len(nums[i])):   # ✅ loop over indices of the inner list
        print(nums[i][j])


numm = [1, 2, 3, 4, 5, 6]

for i in range(1, 5, 2):
    print(numm[i])



or easier way

for row in nums:
    for x in row:
        print(x)



alan = [['Alan','es','chingon','obvio'], ['Anibal' ,'esta','bien'],['Luz','Maria','Mas']]
for row in alan:
    for x in row:
        print(x)



or
 
#enumerate: With enumerate (keeping indices and values)

nums = [[1,2,3], [4,5,6], [7,8,9]]

for i, row in enumerate(nums):
    for j, x in enumerate(row):
        print(f"nums[{i}][{j}] = {x}")




EX:

#Get every pair of elements in array
nums = [1,2,3]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        print(nums[i],nums[j])






EX: insertion sort (insort in middle n times - n2EX: insertion sort (insort in middle n times - n2)
                    






O(2ⁿ) - Exponential: Doubles with each additional input (very slow!)
                                                         










EX:

def find_first(arr):
    return arr[0]

o(1)

Why O(1)?
No matter if the array has 10 items or 10 million items, accessing arr[0] always takes the same amount of time. 
Indexing into an array is a single operation that doesn't depend on the size of the input.


def print_all(arr):
    for item in arr:
        print(item)

This is O(n) because the number of operations grows linearly with the input size. Double the array size, double the time.



def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)



Notice the nested loops? For each item in the outer loop, we run through the entire array again in the inner loop.

If arr has 5 items: 5 × 5 = 25 operations

If arr has 100 items: 100 × 100 = 10,000 operations

This is O(n²) because we're doing n operations n times
          




### 

def mystery(arr):
    if len(arr) == 0:
        return
    print(arr[0])
    mystery(arr[1:])


What's happening?

First call: prints arr[0], then calls itself with arr[1:] (everything except the first element)

Second call: prints the next element, calls itself again

This continues until the array is empty

How many function calls?

If arr has 5 items → 5 function calls

If arr has 100 items → 100 function calls

This is O(n) because the number of recursive calls grows linearly with the input size.

Why Not O(1)?
O(1) means the operation takes the same time regardless of input size. This function clearly does more work with a bigger array—it makes more recursive calls.

Key Insight for Recursion
When analyzing recursion, ask yourself: "How many times does the function call itself?" If it calls itself once for each element, that's O(n).




# o(log n)

EX:
nums = [1, 2, 3, 4, 5]
target = 6
def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    found_index = -1

    while l <= r:
        m = (l + r) // 2

        if target < nums[m]:
            r = m - 1
        elif target > nums[m]:
            l = m + 1
        else:
            found_index = m
            break

    return found_index


# Example usage:
nums = [1, 2, 3, 4, 5]
target = 6

result = binary_search(nums, target)
print(result)  # -1 means not found




#Binary Search on BST

def search(root,target):
    if not root:
        return False
    if target < root.val:
        return search(root.left,target)
    elif target > root.val:
        return search(root.right,target)
    else:
        return True




# Heap Push and Pop
import heapq
minHeap=[]
heapq.heappush(minHeap,5)

its o(log n)






The Key Difference
O(n) processes every element once (like our earlier loop example).

O(log n) cuts the problem in half each time.



How Binary Search Works
Let's trace through an example with arr = [1, 3, 5, 7, 9, 11, 13, 15] and we're searching for 7:

Iteration 1: Check middle (position 4, value = 9). Too high! Eliminate right half.

Remaining: [1, 3, 5, 7] (4 items left)

Iteration 2: Check middle (position 1, value = 3). Too low! Eliminate left half.

Remaining: [5, 7] (2 items left)

Iteration 3: Check middle (position 0, value = 5). Too low! Eliminate left half.

Remaining: [7] (1 item left)

Iteration 4: Found it!

Notice: We started with 8 items and only needed 4 steps.

Why O(log n)?
Each iteration halves the search space:

1000 items → ~10 steps

1,000,000 items → ~20 steps

1,000,000,000 items → ~30 steps


This is logarithmic growth. When input doubles, you only add one more operation.

O(n) vs O(log n)
If this were O(n), searching 1,000,000 items would take 1,000,000 operations. But with O(log n), it takes only ~20! That's the power of logarithmic algorithms.

Common in: binary search, balanced trees



-------------------------------------------------------------------------------------------------------------------------------------------------
# O(n log n) - Linearithmic Time

Common in efficient sorting algorithms.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)



# HeapSort
import heapq
nums = [1,2,3,4,5]
heapq.heapify(nums) #o(n)
while nums:
    heapq.heappop(nums) #o(logn)

Examples: Merge sort, Quick sort (average case), Heap sort.










**ALways talk about best case and worst case complexities **


So the practical answer

For large unordered integer datasets:

merge sort is very efficient
but not always the absolute best choice
in Python, built-in sort()/sorted() is usually preferred




O(n²) - Quadratic Time
Nested loops over the same data.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



Common in: nested loops, simple sorting algorithms





O(n³) - Cubic Time
Three nested loops.



def three_sum(arr):
    result = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if arr[i] + arr[j] + arr[k] == 0:
                    result.append([arr[i], arr[j], arr[k]])
    return result


# Get every triplet of elements in array
nums = [1,2,3]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            print(nums[i],nums[j],nums[k])





O(2ⁿ) - Exponential Time
Doubles with each additional input—very slow!



def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)







Each call makes 2 more calls. With n=30, that's over 1 billion operations!


Recursion, three height n, two branches

def recursion(i,nums):
    if i==len(nums):
        return 0
    
    branch1 = recursion(i+1,nums)
    branch2 = recursion(i+2,nums)




ex:

def recursion(i,nums,c):
    if i == len(nums):
        return 0

    for j in range(i,i+c):
        branch = recursion(j+1,nums)







O(n!) - Factorial Time
Extremely slow—generates all permutations.

def generate_permutations(arr):
    if len(arr) == 0:
        return [[]]
    
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for perm in generate_permutations(rest):
            result.append([arr[i]] + perm)
    return result



With 10 items, that's 3.6 million permutations!









Very important real-world truth

A theoretically “worse” algorithm can outperform a “better” one for small inputs.

Example:

insertion sort is:

O(n
2
)

BUT for tiny arrays it can beat merge sort because:

less overhead
better CPU cache behavior

That’s actually why Python’s Timsort mixes algorithms.








Complete Big O Pattern Guide
O(1) - Constant Time
Pattern: Direct access, no loops or recursion

Examples: Array indexing, hash map lookup, arithmetic operations

Code signal: arr[0], dict[key], return a + b

O(log n) - Logarithmic Time
Pattern: Cutting problem in half (or thirds, etc.) repeatedly

Examples: Binary search, balanced tree operations

Code signal: i = i * 2, i = i / 2, dividing search space each iteration

O(n) - Linear Time
Pattern: Processing every element once

Examples: Simple loop, linear search, finding max/min

Code signal: Single for loop through all elements

O(n log n) - Linearithmic Time
Pattern: Dividing problem AND processing all elements at each level

Examples: Merge sort, heap sort, quicksort (average case)

Code signal: Recursive divide-and-conquer that processes all elements

O(n²) - Quadratic Time
Pattern: Nested loops over the same data

Examples: Bubble sort, selection sort, comparing all pairs

Code signal: Two nested for loops: for i... for j...

O(n³) - Cubic Time
Pattern: Three nested loops

Examples: Triple nested comparisons, 3D matrix operations

Code signal: Three nested for loops

O(2ⁿ) - Exponential Time
Pattern: Making 2 recursive calls each time (branching)

Examples: Naive Fibonacci, generating all subsets, brute force solutions

Code signal: func(n-1) + func(n-2) or similar double recursion

O(n!) - Factorial Time
Pattern: Generating all permutations

Examples: Traveling salesman (brute force), all arrangements

Code signal: Recursive permutation generation

Quick Decision Tree
No loops? → O(1)

Halving/doubling each step? → O(log n)

One loop? → O(n)

Loop + halving pattern? → O(n log n)

Two nested loops? → O(n²)

Three nested loops? → O(n³)

Double recursive calls? → O(2ⁿ)

All permutations? → O(n!)
                      




0(sqrt(n))

# Get all factors of n

import match
n = 12
factors = set()   # Hash set

for i in range(1,int(math.sqrt(n))+1):
    if n % i == 0:
        factors.add(i)
        factors.add(n//i)

print(factors)




0(n!)
  
#Permutations
#Traveling salesman problem






SPACE COMPLEXITY:


Space complexity is how much memory an algorithm needs as a function of its input size.

“Memory” here includes space to store the input itself (input space) plus any extra working storage the algorithm allocates while running (auxiliary space).

In big‑O form, you’ll see expressions like  
O(1)
O(1), 
O
(
log
⁡
n
)
O(logn), 
O
(
n
)
O(n), 
O
(
n
2
)
O(n 
2
 ), 
O
(
2
n
)
O(2 
n
 ), where 
n
n is some measure of input size (number of elements, number of vertices, length of the string, etc.).


In many Python contexts, 
people just say “variable” instead of “scalar variable,” but the idea is the same: if it’s not a list, tuple, dict, set, or array, it’s scalar‑like





When you compute space complexity by hand, you conceptually “count” memory units that grow with 
n
n, ignoring constant factors and machine details



The main contributors:

Variables and constants

A fixed number of scalar variables (ints, pointers, etc.) take constant space.

If your algorithm uses, say, 5 integers and nothing else, that is 
O
(
1
)
O(1) space.


Arrays and collections

An array of length 
n
n uses 
O
(
n
)
O(n) space, assuming each element is constant size.

A 2D array 
n
×
n
n×n uses 
O
(
n
2
)
O(n 
2
 ) space.




Estimation of main memory space requireed to executed an alogorithm 

Space complexity of an algorithm 
= space required to store the source Code + space required for simple variables + space for the data structures used + SPace required for stack for recursive algorithms


the first two are not impportant because they are constants, like time complexity we drop the constants

so 

Space complexity 
= Space for the data structures used [depends on the amount of elements stored in them] + Space required for stack for recursive algorithms [depends on how many times a function is called]





a recursive algorithm is an algo that calls itself within its own body


an interative algorithm : we only focus on the SPace for the data structures used becuase its not a recursie Algorithms ex: loop


ex:

Algo sum(a,n)
{
    sum = 0
    for (i = 1; i <= n; i++)
        sum = sum + a[i]
    return sum
}


-this algo calculates the sum of n elements of a list that being a and n is the size of the list


the only data structure here is a , a list of n elements

space complexity: 0(n)  , there n elements in this list takes n elements of memory space