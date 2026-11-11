# Finding the largest Number
numbers = [10, 25, 5, 40, 15]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)


# Reversing the list
numbers = [1, 2, 3, 4, 5]

reversed_numbers = []

for num in numbers:
    reversed_numbers.insert(0, num)

print(reversed_numbers)


# total sum 
numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total = total + num

print("Sum =", total)


# even odd find
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)


# prime numbers 
n = 7
if n < 2:
    print("Not Prime")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")


# two sum
def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []

nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))


# Second largest unique number
def second_largest(nums):
    largest = float('-inf')
    second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num

    if second == float('-inf'):
        return None

    return second

nums = [10, 5, 20, 8, 20, 15]

print(second_largest(nums))


# anagram
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))


# non-repeating character
from collections import Counter

def first_unique_char(s):
    frequency = Counter(s)

    for i, char in enumerate(s):
        if frequency[char] == 1:
            return i

    return -1

s = "aabbcdde"

print(first_unique_char(s))


# sum of subarray
def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(max_subarray(nums))


# all zeros to the end
def move_zeros(nums):
    position = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[position], nums[i] = nums[i], nums[position]
            position += 1

    return nums

nums = [0, 1, 0, 3, 12]

print(move_zeros(nums))


# Longest Substring Without Repeating Characters
def longest_substring(s):
    last_seen = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        last_seen[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length

s = "abcabcbb"

print(longest_substring(s))


# Binary Search
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

nums = [1, 3, 5, 7, 9, 11]

target = 7

print(binary_search(nums, target))


# Merge Two Sorted Arrays
def is_valid(s):
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in '([{':
            stack.append(char)

        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0

print(is_valid("({[]})"))
print(is_valid("([)]"))

def is_valid(s):
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in '([{':
            stack.append(char)

        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0

print(is_valid("({[]})"))
print(is_valid("([)]"))



# find the missing number:
def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum


nums = [3, 0, 1]
print(missing_number(nums))

