'''
Write a function burgerPrice(burger) to take in a string of customization and return a total sum for 
the price

Using dictionary/lookup table
'''
def burgerPrice(burger):
    total=[]
    price={'B':0.5,'C':0.8,'P':1.5,'V':0.7,'O':0.4,'M':0.9}
    for i in burger: total.append(price[i])
    return sum(total)
 


print(burgerPrice('BVPB'))
print(burgerPrice('BVCPCPB'))
print(burgerPrice('BPVBPVCB'))

'''
Check anagram using dictionary by creating histogram/frquency count
'''
def is_anagram1(word1,word2): #verbose version
    d1,d2={},{}
    for i in word1.replace(' ',''):
        if i not in d1: d1[i]=1
        else: d1[i]+=1
    for j in word2.replace(' ',''):
        if j not in d2: d2[j]=1
        else: d2[j]+=1
    if d1==d2: return True
    else: return False
    
def is_anagram2(word1,word2): #use .get so no need to use if
    d1,d2={},{}
    for char in word1.replace(' ',''):
        d1[char]=d1.get(char,0)+1
    for char in word2.replace(' ',''):
        d2[char]=d2.get(char,0)+1
    if d1==d2: return True
    else: return False
    
def is_anagram3(word1,word2):
    d1,d2={},{}
    for char in word1.replace(' ',''):
        d1[char]=d1.get(char,0)+1
    for char in word2.replace(' ',''):
        d2[char]=d2.get(char,0)+1
    return d1==d2 # straightaway return the evaluated comparison, no need to use if