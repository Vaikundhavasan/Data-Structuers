import math
print("Distance Between Two Points")

x1 = int(input("Enter value for x1 : "))
x2 = int(input("Enter value for x2 : "))
y1 = int(input("Enter value for y1 : "))
y2 = int(input("Enter value for y2 : "))

x=x2-x1
y=y2-y1

D1=x**2
D2=y**2

D3=D1+D2

D=math.sqrt(D3)

print("Distance Between Two Points : ",D)
