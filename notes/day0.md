## Day 0

This is Day 0 for setting up the Github repo & VSC


Test: For the solution to [99 Problems](https://open.kattis.com/problems/99problems) ,see below:

```
N=float(input())
if N <100: 
    print(99)
else:
    N += 1.1
    print((round(N/100)*100)-1)
```
This is the solution to [ABC](https://open.kattis.com/problems/abc) :

```
num=sorted(map(int,input().split()))
order=input()
res=[]
for i in order:
    if i == 'A':
        res.append(num[0])
    elif i == 'B':
        res.append(num[1])
    elif i == 'C':
        res.append(num[2])
print (' '.join(str(x) for x in res))
```