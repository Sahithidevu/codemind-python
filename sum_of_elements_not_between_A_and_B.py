n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
d=[]
for i in range(n):
    if a[i]>=x and a[i]<=y:
        pass
    else:
        d.append(a[i])
print(sum(d))