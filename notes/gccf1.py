'''
Write a function burgerPrice(burger) to take in a string of customization and return a total sum for 
the price
'''
def burgerPrice(burger):
    total=[]
    price={'B':0.5,'C':0.8,'P':1.5,'V':0.7,'O':0.4,'M':0.9}
    for i in burger: total.append(price[i])
    return sum(total)
 


print(burgerPrice('BVPB'))
print(burgerPrice('BVCPCPB'))
print(burgerPrice('BPVBPVCB'))