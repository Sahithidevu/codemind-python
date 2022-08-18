n=int(input())
arr=list(map(int,input().split()))
sum=0
for i in range(0,n):
    sum+=arr[i]
avg=sum/n
print(format(avg,'.2f'))