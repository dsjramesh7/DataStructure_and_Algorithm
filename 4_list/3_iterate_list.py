random = [1, "hello", 3,4,5,"World"]

# iterating over list 
for value in random:
  print(value)

# getting index and the value 
for index,value in enumerate(random):
  print(f"index= {index}, value= {value}")

# list comprehension
list1 = []
for i in range(10):
  list1.append(i**2)
print(list1)

# list comprension eg:
cubeList = [i**3 for i in range(12)]
print(cubeList)

even_numbers = [num for num in range(10) if num%2==0]
print(even_numbers)

# in function call list comprehension
words = ["I", "Am", "The", "Greatest"]
lengthEachWord = [len(word) for word in words]
print(lengthEachWord)