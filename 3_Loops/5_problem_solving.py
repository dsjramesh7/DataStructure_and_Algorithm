# =============== Solving coding problems =======================

# 1 => Calculate the sum of N natural numbers using a while and for loop
num = int(input("Enter a number: "))
# # while loop ke through
count = 1
sum = 0
while count <= num:
  sum = sum + count
  count = count + 1
print(f"Sum of {num}th natural number is {sum}")

# # for loop ke through
result = 0
for i in range(num+1):
  result = result + i
print(result)



# 2 => get all the prime number from 1 to 100
for num in range(1,101):
  if num>1:
    for i in range (2, num):
      if num%i==0:
        break
    else:
      print(num)