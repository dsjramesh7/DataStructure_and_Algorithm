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