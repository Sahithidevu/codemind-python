n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
lst=[]
for i in range(len(arr)):
    if a<=arr[i] and b>=arr[i]:
        pass
    else:
        lst.append(arr[i])
if len(lst)!=0:
    print(max(lst))
else:
    print(-1)