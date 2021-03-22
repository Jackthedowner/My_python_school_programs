l=[]
listofindex=[]
size=int(input("enter size of list:"))
for i in range(0,size): #index
    if i!=0:
       h=-i
       print(h) #h=-1
       listofindex.append(h)
    print(i)    #i=0
    listofindex.append(i)

for k in range(1,size+1):
    l.insert(listofindex[k-1],k) #k=1     #inserting values
    print('k',k)
l.reverse()
print('listofindex',listofindex)
print('final list:',l)
