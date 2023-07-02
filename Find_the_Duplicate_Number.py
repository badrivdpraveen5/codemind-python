from collections import Counter 
a=int(input())
l=list(map(int,input().split()))
d=dict(Counter(l))
for i in d:
    if d.get(i)!=1:
        print(i)