n,k=map(int,input().split())
a=list(map(int,input().split()))
c=[]
for i in range(n):
    if a[i]%k!=0:
        c.append(a[i])
print(len(c))