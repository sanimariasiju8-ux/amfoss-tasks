## 1. Two Sum

### Problem :
 You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Approach
Used a dictionary to remember numbers that already encountered. For each number, calculate target - num and check whether that required number is already stored.

Code explanation:
seen = {} creates the dictionary.
enumerate(nums) gives us both the index and value.
needed = target - num finds the complement.
if needed in seen checks whether the complement was already encountered.
seen[num] = i stores the current number and its index.

### What I learned
I learned how a dictionary can make searching for a required value much faster. Instead of checking every possible pair, I can store previously visited numbers and directly check whether the required complement already exists.

## 2. Valid Parantheses

### Problem
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type

### Approach
I used a stack because brackets follow the Last In, First Out (LIFO) principle.
When an opening bracket is encountered, I put it into the stack.
When a closing bracket is encountered, I check whether it matches the most recently opened bracket, which is at the top of the stack.
For example: ([{}])
The opening order is: ( → [ → {
Therefore, the closing order must be: } → ] → )
If a closing bracket doesn't match the top of the stack, the string is invalid.

Code explanation:
stack = []
Creates an empty stack.
pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}
Stores the matching opening bracket for every closing bracket.
for bracket in s:
Checks each bracket one by one.
For an opening bracket:
stack.append(bracket)
It is pushed onto the stack.
For a closing bracket:
if not stack or stack[-1] != pairs[bracket]:
    return False
It checks whether the stack is empty or whether the top bracket doesn't match.
If it matches:
stack.pop()
It removes the matched opening bracket.
Finally:
return len(stack) == 0
If the stack is empty, every bracket was matched correctly.

### What I learned 
I learned how a stack follows the Last In, First Out principle and how this makes it useful for problems involving nested or matching elements. I also learned how to use a dictionary to map closing brackets to their corresponding opening brackets.

## 3. Palindrome Number

### Problem
Given an integer x, determine whether it reads the same from left to right and right to left.
Example:
121 → True
1221 → True
123 → False
-121 → False

### Approach
I used:
% 10 to get the last digit
// 10 to remove the last digit
* 10 to build the reversed number
I first store the original number. Then I repeatedly take the last digit and add it to reversed_num.

Code explanation:
if x < 0:
    return False
Negative numbers are not considered palindromes.
original = x
reversed_num = 0
It saves the original number and start building its reverse.
digit = x % 10
Gets the last digit.
Then:
reversed_num = reversed_num * 10 + digit
Adds that digit to the reversed number.
Finally:
x = x // 10
Removes the last digit from x.
The process continues until there are no digits left.
At the end:
return original == reversed_num
If both numbers are equal, the number is a palindrome.

### What I learned
I learned how to manipulate individual digits using mathematical operations such as modulo (%) and integer division (//). I also learned that a problem involving a number does not always require converting it into a string; it can sometimes be solved directly using arithmetic operations.

## 4. Longest Substring Without Repeating Characters

### Problem
Given a string s, find the length of the longest substring that contains no repeated characters.
A substring must contain continuous characters from the original string.
Example:
"abcabcbb" → 3
"bbbbb"    → 1
"pwwkew"   → 3

### Approach
I used the Sliding Window technique with a set.
The window is represented using two pointers:
left  → beginning of the current substring
right → end of the current substring
The set stores the characters currently inside the window.
We move right through the string:
If the current character hasn't appeared in the window, we add it.
If it is already present, there is a duplicate.
We then move left forward and remove characters until the duplicate is removed.
At every step, we calculate the current window length and keep track of the maximum length.

Code explanation:
seen = set()
left = 0
max_length = 0
seen stores the characters currently in the window.
left represents the starting position.
max_length stores the longest valid substring found so far.
for right in range(len(s)):
Moves right through every character in the string.
When a duplicate is found:
while s[right] in seen:
    seen.remove(s[left])
    left += 1
It removes characters from the left until the duplicate is no longer in the window.
Then:
seen.add(s[right])
adds the current character.
The current window length is calculated using:
current_length = right - left + 1
The maximum length is updated with:
max_length = max(max_length, current_length)
Finally:
return max_length
returns the length of the longest substring without repeated characters.

### What I learned
I learned how the Sliding Window technique can efficiently process a continuous section of a string. I also learned how two pointers and a set can work together to detect duplicates and maintain a valid window without repeatedly checking the entire substring.

## 5. 3Sum

### Problem
Given an integer array nums, find all unique triplets whose sum is equal to 0.
Example:
nums = [-1, 0, 1, 2, -1, -4]
The valid triplets are:
[-1, -1, 2]
[-1, 0, 1]
So the output is:
[[-1, -1, 2], [-1, 0, 1]]

### Approach
I use sorting + two pointers.
First, I sort the array and then I fix one number at a time and use two pointers to find the other two numbers.
We calculate:
total = nums[i] + nums[left] + nums[right]
Then:
If total == 0 → we found a valid triplet.
If total < 0 → move left forward to increase the sum.
If total > 0 → move right backward to decrease the sum.

Code explanation:
nums.sort()
Sorts the array, which allows us to use the two-pointer technique.
Then:
for i in range(len(nums) - 2):
Fixes one number of the triplet.
To skip duplicate values:
if i > 0 and nums[i] == nums[i - 1]:
    continue
This prevents generating the same triplet more than once.
Then to initialize the two pointers:
left = i + 1
right = len(nums) - 1
Now to calculate the sum:
total = nums[i] + nums[left] + nums[right]
If the sum is zero:
if total == 0:
    result.append([nums[i], nums[left], nums[right]])
It save the triplet.
After finding a triplet, we skip duplicate values for both pointers so that the result contains only unique triplets.
If the sum is too small:
elif total < 0:
    left += 1
we increase left.
If the sum is too large:
else:
    right -= 1
we decrease right.
Finally:
return result
returns all unique triplets.

### What I learned
I learned how sorting can help simplify a problem and make the two-pointer technique possible. I also learned how moving two pointers based on the current sum can avoid unnecessary comparisons. Handling duplicate values taught me the importance of carefully controlling the output when only unique solutions are required.

## Overall Learning
Through these five LeetCode problems, I learned that solving a programming problem is not just about getting the correct answer. Choosing the right data structure and algorithm can make a solution much more efficient.
The main concepts I learned were:
Hash Maps — storing previously seen values to find the required value efficiently.
Stacks — using the Last In, First Out (LIFO) principle to handle nested and matching brackets.
Number Manipulation — using % and // to work with individual digits without converting the number to a string.
Sliding Window — using two pointers and a set to efficiently process a continuous part of a string.
Sorting and Two Pointers — reducing the amount of unnecessary searching in the 3Sum problem.

Most importantly, these problems taught me to understand the problem first, identify the right technique, and then write the code. I also learned that a solution that works is not always the best solution; improving its efficiency and being able to explain the reasoning behind it are equally important.

