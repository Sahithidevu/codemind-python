n=int(input())
t=n
sum=0
while n>0:
    r=n%10
    fact=1
    for i in range(1,r+1):
        fact=fact*i
    sum+=fact
    n=n//10
if sum==t:
    print('The number',t,'is a strong number')
else:
    print('The number',t,'is not a strong number')