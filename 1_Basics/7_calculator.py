## Simple Calculator

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter First Number: "))

if num1<0 and num2<0:
  print("Don't give negative numbers")
else:
  sum = num1 + num2
  difference = num1 - num2
  multiply = num1 * num2
  divide = num1 / num2

print("Sum: ", sum)
print("Difference: ", difference)
print("Multiply: ", multiply)
print("Divide: ", divide)