arr = [1,2,3,4,5]

for i in range(0,len(arr)):
  for j in range(i+1, len(arr)):
    print('({},{})'.format(arr[i],arr[j]))


# O(n^2)