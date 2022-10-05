n=int(input())
a=list(map(int,input().split()))
l=[]
if n%2!=0:
    a.append(0)
for i in range(len(a)):
    l.append(a[i])
    print(l[i],end=' ')