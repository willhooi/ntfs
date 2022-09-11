## What did I learn?

1.  Understand the problem first before jumping straight to coding

2. Always look for the base case/smallest block when solving 'reductive' problems esp using recursion

3. Use dictionary to speed up search e.g. fibonacci(n)

```
known={0:0,1:1}

def fibonacci(n):
    if n in known:
        return known[n]
    else:
        res = fibonacci(n-1)+fibonacci(n-2)
        known[n]=res
        return res
        
```