n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in range(len(arr)):
    if a<=arr[i] and b>=arr[i]:
        pass
    else:
        c.append(arr[i])
        
if len(c)!=0:
    print(min(c))
else:
    print(-1)