def intToStr(i):
  digits = "0123456789"
  if i == 0:
    return 0
  result = ""
  while i > 0:
    result = digits[i % 10] + result
    i = i // 10
  return result

print(intToStr(123))
print(type(intToStr(123)))
print(2)
print(type(2))

# logn the best 