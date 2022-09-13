n=int(input())
a=list(map(int,input().split()))
c=[]
for i in a:
    i=abs(i)
    tmp=len(str(i))
    c.append(tmp)
print(*c)