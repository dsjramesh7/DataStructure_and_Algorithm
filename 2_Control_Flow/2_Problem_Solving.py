# Determin the year is leap or not 
year = int(input("Tell the year to check if its a leap year: "))

if year>=1000:
  print("Good Boy, Now let's check other condition!!!")
  if year%4==0:
    print(str(year) + " year is a leap year")
  else:
    print(str(year) + " year is not a leap year")
else:
  print("Bad Boyt, The year is negative or zero or any other thing please try again")
  