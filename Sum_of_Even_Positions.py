n=int(input())
arr=list(map(int,input().split()))
evensum=0
for i in range(0,n):
    if i%2==0:
        evensum+=arr[i]
print(evensum)