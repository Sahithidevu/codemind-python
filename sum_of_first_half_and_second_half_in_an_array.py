n=int(input())
a=list(map(int,input().split()))
sum1=0
sum2=0
c=n//2
for i in range(0,c):
    sum1+=a[i]
for i in range(c,n):
    sum2+=a[i]
print(sum1)
print(sum2)