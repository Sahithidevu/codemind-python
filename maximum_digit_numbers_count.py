n=int(input())
a=list(map(int,input().split()))
c=[]
d=[]
for i in range(n):
    c.append(len(str(a[i])))
tmp=max(c)
for i in range(n):
    if tmp==c[i]:
        d.append(a[i])
print(*d)