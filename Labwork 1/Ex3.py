n = int(input("Enter num:"))
prime = True
for i in range(2,n):
  if n%i == 0:
    prime = False
    break
if prime:
  print(n,"is a prime number")
else:
  print(n,"is NOT a prime number")