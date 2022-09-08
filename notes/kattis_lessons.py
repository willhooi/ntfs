'''
https://open.kattis.com/problems/electricaloutlets

example of using map() to apply int() to list elements
-map() returns an object -> needs to be 'consumed' with list()
-use test[1:] to only get items from index 1 onwards

as discussed in IT5001
'''

def eoutlets():
    N = int(input())
    for i in range(N):
        test=list(map(int,input().split()))
        print((sum(test[1:])-test[0])+1)
        
eoutlets()
