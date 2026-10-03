# Advanced Calculator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter first number: "))

operations = input("Enter operations (+ , - , * , /): ")

if(num1 >= 0 and num2>=0):
  print("Numbers are positive good human")
  if(operations == '+'):
    result = num1 + num2
  elif(operations == '-'):
    result = num1 - num2
  elif(operations == '*'):
    result = num1 * num2
  elif(operations == '/'):
      if(num2 != 0):
        result = num1 / num2
      else:
        result = "Error! Division by zero"
  else:
    result = "Invalid opertions, Try again!!!"
else:
  result = "Bad Human , The number is negative or any other thing please try again"
  


print("Result: ", result)

