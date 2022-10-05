n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(len(a)):
    if a[i]%2!=0:
        sum+=a[i]
    else:
        break
print(sum)