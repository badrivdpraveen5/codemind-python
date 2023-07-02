a=input()

x=y=0

for i in a:

    if i == 'L':

        x-=1

    elif i == 'R':

        x+=1

    elif i == 'U':

        y+=1

    else:

        y-=1

print(x==0 and y==0)