n=int(input())
l=list(map(int,input().split()))
temp=[]
for i in l:
    if i not in temp:
        temp.append(i)
print(*temp)
        