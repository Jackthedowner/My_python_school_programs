#write a program to calculate simple and compound interest by using input.
#declaration of global variables
price=int(input("Enter your price(in rupees):"))
rate=int(input("Enter your rate(in percent):"))
time=int(input("Enter your time(in years):"))
n=int(input("Enter your n:"))
#function
si=(price*rate*time)/100
ci=(price*(1+rate/100)**n)-price
#display
print("Your simple interest is,",si)
print("Your compound interest is,",ci)

