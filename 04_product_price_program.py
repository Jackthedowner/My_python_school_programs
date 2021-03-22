n=int(input('Enter how many product:'))
items={}
for i in range(0,n):
    product=input('Enter Product Name:')
    price=int(input('Enter price of product:'))
    items[product]=price
print('items','=',items)
k=input('Enter Product Name:')
for p in items:
    if k==p:
       print(items.get(k))