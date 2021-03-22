l=[]
x=0
while x<3:
      k=int(input('Enter Number:'))
      l.append(k)
      x=x+1
print('original list:',l)
n=len(l)

for i in range(n):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
           l[j],l[j+1]= l[j+1],l[j]
print('final sorted list of numbers is:', l)
           
        
