n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(n):
    rev=int(str(a[i])[::-1])
    if a[i]==rev:
        c.append(a[i])
print(len(c))