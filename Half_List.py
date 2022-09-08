n=int(input())
a=list(map(int,input().split()))
d=[]
for i in range(n//2,n):
    d.append(a[i])
d.reverse()
for i in range(n//2):
    d.append(a[i])

for i in range(len(d)):
    print(d[i],end=' ')