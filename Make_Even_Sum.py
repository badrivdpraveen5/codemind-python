n=int(input())
a=list(map(int,input().split()))
oc=0
for i in a:
    if i%2!=0:
        oc+=1
if(oc%2==0 and (n-oc)%2==0):
    print(1)
else:
    print(0)