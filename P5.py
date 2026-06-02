a=[1,2,3,4]
b=[3,7,4,9,10]

for i in a:
  for j in b:
    if i < j:
      print('({},{})'.format(i,j))

  
#O(ab)