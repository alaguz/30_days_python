Roman to Int LeetCode

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].



## Edge Cases (Testing boundaries and extremes)
test_minimum_value: Tests the smallest possible Roman numeral (1) - this is at the lower boundary

test_maximum_value: Tests the largest possible Roman numeral (3999) - this is at the upper boundary

test_single_character: Tests the minimum length constraint (length = 1) - boundary condition

test_all_subtractive_pairs: Tests every possible subtractive combination, which is a critical pattern that could break the algorithm if the comparison logic fails

## Regular Test Cases (Standard functionality)
test_simple_addition: Tests a straightforward case like "III" = 3 where we're just adding values - this is typical behavior, not at any boundary

test_complex_mixed: Tests "MCMXCIV" (1994) - while complex, it's a middle-range value that exercises the logic but isn't at any extreme



class Solution:
    def romanToInt(self, s: str) -> int:
        # VALIDATION FIRST - before any processing     --> Its called input validation
        # Step 1: Check if input is a string
        if not isinstance(s, str):
            raise TypeError(f"Input must be a string, got {type(s).__name__}")
        
        # Step 2: Check if string is not empty
        if not s:
            raise ValueError("Input string cannot be empty")
        
        # Step 3: Check if all characters are valid Roman numerals
        valid_chars = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
        for char in s:
            if char not in valid_chars:
                raise ValueError(f"Invalid Roman numeral character: '{char}'")
        
        # NOW proceed with the actual algorithm
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s)):
            value = values[s[i]]
            # Look ahead to the next value, if it exists
            if i + 1 < len(s) and value < values[s[i + 1]]:
                total -= value
            else:
                total += value

        return total


# Create an instance of the Solution class
solution = Solution()

# Now call the method on that instance
result = solution.romanToInt("ABC")

result = solution.romanToInt("")

result = solution.romanToInt("III")
print(result)  # This will print 3

result_1 = solution.romanToInt("I")
print(result_1)









Answer:


1. Start with the Problem Statement
"This algorithm converts Roman numerals to integers. The key challenge is handling subtractive notation—where a smaller numeral before a larger one means subtraction, like IV = 4".

2. Explain the Approach at a High Level
"I'm using a single-pass algorithm that processes the string left to right. The core insight is: if the current value is less than the next value, subtract it; otherwise, add it".

3. Walk Through the Code Logic
"The dictionary maps each Roman character to its value. Then I iterate through each character, comparing it with the next one. The condition i + 1 < len(s) prevents index out-of-bounds errors, and value < values[s[i + 1]] detects subtractive cases".

4. Provide a Concrete Example
"For 'IX' which equals 9: At index 0, 'I' = 1, and the next is 'X' = 10. Since 1 < 10, we subtract: total = -1. At index 1, 'X' = 10, no next character, so we add: total = -1 + 10 = 9".

5. Discuss Time and Space Complexity
"This runs in O(n) time where n is the string length, and O(1) space since the dictionary is constant size".

6. Mention Edge Cases or Improvements
"Edge cases would include empty strings or invalid Roman numerals. We could add validation to check for those".






The algorithm is saying: "When a small numeral comes before a large one, "
"that small numeral is 'negative' in our running sum". So 'I' in "IV" contributes -1 to the total, while 'V' contributes +5, giving us 4






explain:


#Intuition
The key observation is that Roman numerals are usually additive (values are summed), but sometimes subtractive when a smaller numeral comes before 
a larger one (like IV = 4 or IX = 9).

So, for each character, it is enough to compare its value with the value of the next character to decide whether to add or subtract.

#Approach
Create a dictionary values that maps each Roman symbol (I, V, X, L, C, D, M) to its integer value.

Initialize a running total total = 0.

Loop over the string by index. For each character at index i:

Get its value value = values[s[i]].

If there is a next character, and value < values[s[i+1]], then this is a subtractive case (like IV, IX), so subtract value from total.

Otherwise, add value to total.

After processing all characters, return total as the integer value.

This works because every subtractive pair is handled by the “look ahead one character and compare” rule, and all other characters are simply added.

#Complexity
Time complexity:
The loop goes through each character of the string exactly once, and each step does constant-time work (a few dictionary lookups and comparisons).
So the time complexity is

O(n)
O(n)
where 
n
n is the length of the input string.

#Space complexity:
The dictionary values has a fixed size of 7 entries, independent of the input length, and aside from that only a few scalar variables are used.

So the extra space used is O(1)
O(1)
constant space.





Time and Space Complexity Analysis
Time Complexity: O(n)

We loop through the string once using for i in range(len(s))

Each iteration does constant-time operations: dictionary lookup values[s[i]], comparison, and addition/subtraction

So: n iterations × O(1) work per iteration = O(n)

Space Complexity: O(1)

The values dictionary has 7 fixed entries—it doesn't grow with input size

Variables like total, i, and value are just a few integers

No additional data structures scale with input size

So: O(1) constant space

How to Say This in an Interview
Use this template:

"My solution is O(n) time and O(1) space.

The time comes from a single pass through the string, where each character is processed once with constant-time dictionary lookups and arithmetic operations.

The space comes from the fixed-size dictionary and a few scalar variables—nothing that scales with the input size."



Can We Optimize Further?
Short answer: Not really.

Here's what you'd say in an interview:

"This solution is already optimal. We must read every character at least once to compute the result, so O(n) time is the theoretical lower bound. The space complexity is already constant, which is optimal. Any 'optimization' would be micro-optimizations that don't change the Big O complexity".







Why We Can't Do Better Than O(n) Time
The Information-Theoretic Lower Bound

To convert a Roman numeral to an integer, we must examine every character at least once. Here's why:

If we skip even one character, we could miss critical information

Example: "IX" vs "XI" — they differ by only one character position, but give different results (9 vs 11)

We can't know the final answer without reading all input

Think of it this way: You can't summarize a book without reading it.

In interview terms, you'd say:

"We cannot do better than O(n) because we must process every character at least once. This is called the information-theoretic lower bound—the minimum work required to solve the problem. Skipping any character could lead to an incorrect result".

Why We Can't Do Better Than O(1) Space
We're Already Using Minimal Space

Our space usage is:

A fixed-size dictionary (7 entries)

A few scalar variables (total, i, value)

None of these grow with input size. We're already optimal.

You could theoretically use zero extra space if you computed Roman values inline with if-statements instead of a dictionary, but that would be O(1) as well—constants don't matter in Big O.