#List
container = ["mat", 1,2,3, True, "drinks"]
print(type(container))
print(container)

# accessing the value
print(container[0])
print(container[3])
print(container[-1])
print(container[4])
print(container[3:])
print(container[1:3])
print(container[:5])

# updating the value 
container[0] = "Luffy Toy"
container.append("last Apple")
print(container)

# inserting the value
container.insert(1,"apple")
container.insert(5,"apple")
print(container)

# remove at first occurence
container.remove("drinks")
print(container)

# pop remove the last value
popped_value = container.pop()
print(popped_value)
print(container)

# find the value 
print(container.index("Luffy Toy"))

# count how many times the value is there 
print(container.count("apple"))
print(container.count("Luffy Toy"))
print(container.count(1))
print(container.count(2))





