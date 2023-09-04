n=int(input())
r=[]
l=list(map(int,input().split()))
for i in l:
    if i==1:
        r.append(i)
    else:
        r.insert(0,i)
print(*r)