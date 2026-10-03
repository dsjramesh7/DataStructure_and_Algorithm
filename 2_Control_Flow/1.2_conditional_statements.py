num = int(input("Enter your Number: "))
# nested if else 

if num>0:
  print("Good Girl, The number is positive number so going to check other condition")
  if num%2==0:
    print("The number is even")
  else:
    print("The number is odd")
else:
  print("Bad Girl, The number is negative or zero or any other thing please try again")
  