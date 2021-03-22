#write a program to input 3 sides of a triangle and check triangle is form or not.
import math
#declaration
a=int(input("Enter Side :"))
b=int(input("Enter Side :"))
c=int(input("Enter Side :"))
#function
s=((a+b+c)/2)
print(s)
area=math.sqrt(s*(s-a)+s*(s-b)+s*(s-c))
print(area)
#condition
if area!=0:
    print("a,b,c is a triangle")
else:
    print("a,b,c is not a triangle")
#display
print(s)
