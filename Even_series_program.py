def ev(n):
    listofEven=[]
    listofall=[]
    print('ALL NUMBERS:→')
    for i in range(0,n+1):
        print(i,end=' ')
        listofall.append(i)
    print('List of All Numbers:',listofall)
    print('EVEN NUMBERS→')
    for i in range(0,n+1,2):
        print(i,end=' ')
        listofEven.append(i)  
    print('List of Even Numbers:', listofEven)
    print('Sum of list is:',sum(listofEven))
n=int(input('how many times:'))

ev(n)