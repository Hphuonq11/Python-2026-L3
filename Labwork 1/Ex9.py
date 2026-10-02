n = int(input("Enter a number:"))
def factorial(n):
  if n < 0:
    return "Not defined"

  result=1
  for i in range(1, n+1):
    result *=i
  return result
print(factorial(n))