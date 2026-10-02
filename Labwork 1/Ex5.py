x= str(input("What is your favourite color? "))
Colors = ['Pink','Yellow','Blue','Red','Orange']

if x in Colors:
  print("Your color is at index",Colors.index(x),"in my list")
else:
  print("Sorry, I could not find your color")

