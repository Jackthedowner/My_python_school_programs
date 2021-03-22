s='happy'
print(s)
l=len(s)
j=int((len(s)+1)/2)
for i in range(0,len(s)):
    if i==j:
       print(s[0:i-1]+' '+s[i:l+1])
    elif i==j+1:
       print(s[0:i-j]+' '*j+s[-1])