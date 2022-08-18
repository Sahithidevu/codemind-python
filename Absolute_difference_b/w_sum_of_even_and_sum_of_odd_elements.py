n=int(input())
arr=list(map(int,input().split()))
evsum=0
odsum=0
for i in range(0,n):
    if arr[i]%2==0:
        evsum+=arr[i]
    else:
        odsum+=arr[i]
res=abs(evsum-odsum)
print(res)