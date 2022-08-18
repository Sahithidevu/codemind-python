n=int(input())
arr=list(map(int,input().split()))
evensum=0
oddsum=0
for i in range(0,n):
    if i%2==0:
        evensum+=arr[i]
    else:
        oddsum+=arr[i]
res=abs(evensum-oddsum)
print(res)