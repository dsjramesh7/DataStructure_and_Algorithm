# loop control statements
# break statement
for i in range (15):
  if i==13:
    break
  print(i)


#continue statement
for i in range(15):
  if i%2==0: # here we can say we are trying to get even but..
    continue # skipping the current iteration and the program continues got it
  print(i) # you will see we are getting odd numbers 
