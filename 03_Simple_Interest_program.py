principle=[]
rate=[]
time=[]
ST=[]
n=int(input('how many times:'))
for i in range(0, n):
	 p=int(input('Enter Principle:'))
	 r=int(input('Enter Rate:'))
	 t=int(input('Enter Time:'))
	 principle.append(p)
	 rate.append(r)
	 time.append(t)
	 Si=int((p*r*t)/100)
	 ST.append(Si)
print('List of Principle:', principle)
print('List of Rate:', rate)
print('List of Time:', time)
print('List of Simple Interest',ST)
print('P,R,T,SI ')
for k in range(0, n):
      print(principle[i],rate[i], time[i], ST[i])