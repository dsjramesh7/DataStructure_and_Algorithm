my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))

my_emptySet = set()
print(my_emptySet)
print(type(my_emptySet))

my_listInside_set = set([1,2,3,4,5,6])
print(my_listInside_set)
print(type(my_listInside_set))


#add 
my_set.add(7)
print(my_set)
#even if you try to add same element again it would give one time element
my_set.add(7)
print(my_set)

#remove
my_set.discard(1)
print(my_set)