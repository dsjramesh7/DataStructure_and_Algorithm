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