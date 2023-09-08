n=int(input())
fare=0
w=[]
for i in range(n):
    w.append(int(input()))
t=int(input())
for i in w:
    if i<=t:
        fare+=1
    else:
        fare+=2
print(fare)