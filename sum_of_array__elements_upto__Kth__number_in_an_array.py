n=int(input())
a=list(map(int,input().split()))
k=int(input())
sum=0
for i in range(len(a)):
    if a[i]==k:
        sum+=k
        break
    else:
        sum+=a[i]
print(sum)