def fib(n):
  a=0
  b=1
  c=0
  listfib=[0,1]
  for i in range(2,n):
      c=a+b
      a=b
      b=c
      listfib.append(c)
  print('Original list of fibonacci:',listfib)
  listfib.reverse()
  print('Reversed list of fibonacci number:',listfib)
r=int(input("Enter range to print fibonacci series:"))
fib(r)






