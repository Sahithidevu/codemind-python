n=int(input())
a=list(map(int,input().split()))
l1=[]
l2=[]
for i in range(n):
    if a[i]%2!=0:
        l1.append(a[i])
for i in range(n):
    if a[i]%2==0:
        l2.append(a[i])
p=l1+l2
for i in p:
    print(i,end=' ')