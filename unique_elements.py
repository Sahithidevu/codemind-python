n=int(input())
lst=list(map(int,input().split()))
c=[]
for i in range(n):
    if lst[i] in c:
        continue
    else:
        c.append(lst[i])
for i in range(len(c)):
    print(c[i],end=' ')