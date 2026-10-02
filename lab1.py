#Ex1
r = float(input("Enter circle radius:"))
area=3.14*(r**2)
print("Circle area =", round(area, 0))

#Ex2
t = float(input("Enter the temperature in Celcius:"))
result = t*1.8+32
print("Temperature in Fahrenheit =", result)

#Ex3
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

  #Ex4
n=int(input("Enter a number:"))
sum = 0 #sum all divisors
for i in range(1,n):
  if n % i == 0:
   sum +=i

if sum == n:
  print(n,"is a perfect number")
else:
  print(n,"is a NOT perfect number")

  #Ex5
  x= str(input("What is your favourite color? "))
Colors = ['Pink','Yellow','Blue','Red','Orange']

if x in Colors:
  print("Your color is at index",Colors.index(x),"in my list")
else:
  print("Sorry, I could not find your color")

#Ex6
