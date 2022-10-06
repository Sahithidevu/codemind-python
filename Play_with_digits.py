n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(0,n):
    tmp=0
    while a[i]:
        r=a[i]%10
        tmp+=r
        a[i]//=10
    sum+=tmp
print(sum)