n=int(input())
a=list(map(int,input().split()))
c=[]
for i in a:
    if i not in c:
        c.append(i)
c=sum(c)
print(c)