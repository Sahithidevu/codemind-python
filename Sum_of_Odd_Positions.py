n=int(input())
arr=list(map(int,input().split()))
oddsum=0
for i in range(0,n):
    if i%2!=0:
        oddsum+=arr[i]
print(oddsum)