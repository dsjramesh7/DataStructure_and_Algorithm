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