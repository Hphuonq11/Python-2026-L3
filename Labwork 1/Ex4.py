n=int(input("Enter a number:"))
sum = 0 #sum all divisors
for i in range(1,n):
  if n % i == 0:
   sum +=i

if sum == n:
  print(n,"is a perfect number")
else:
  print(n,"is a NOT perfect number")