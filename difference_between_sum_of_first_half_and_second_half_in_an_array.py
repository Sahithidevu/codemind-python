n=int(input())
a=list(map(int,input().split()))
c=n//2
sum1=0
sum2=0
for i in range(0,c):
    sum1+=a[i]
for i in range(c,n):
    sum2+=a[i]
print(abs(sum1-sum2))