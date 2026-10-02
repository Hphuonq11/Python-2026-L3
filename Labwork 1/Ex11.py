import math
def dis_two_point(x1,y1,x2,y2):
  return math.sqrt((x2-x1)**2+(y2-y1)**2)
x1=float(input("Enter x1:"))
y1=float(input("Enter y1:"))
x2=float(input("Enter x2:"))
y2=float(input("Enter y2:"))
print(dis_two_point(x1,y1,x2,y2))