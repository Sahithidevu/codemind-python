n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(n):
    rev=int(str(a[i])[::-1])
    c.append(rev)
print(*c)