n,k=map(int,input().split())
a=list(map(int,input().split()))
c=[]
for i in a:
    i=abs(i)
    tmp=len(str(i))
    if tmp==k:c.append(tmp)
print(len(c))