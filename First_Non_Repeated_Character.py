t=int(input())

for i in range(t):

    a=int(input())

    s=input()

    for i in s:

        if i not in s[s.index(i)+1:]:

            print(i)

            break

    else:

        print(-1)
