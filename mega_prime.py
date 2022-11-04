n=int(input())
l=len(str(n))
a=[2,3,5,7]
b=0
count=0
for i in range(2,int(n**.5)+1):
    if n%i==0:
        break
else:
    b=True
if b==True:
    while n:
        r=n%10
        if r in a:
            count+=1
        n//=10
    if l==count:
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')