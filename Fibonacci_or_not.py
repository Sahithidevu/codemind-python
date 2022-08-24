n=int(input())
c=0
a,b=0,1
if n==0 or n==1:
    print('True')
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if n==c:
        print('True')
    else:
        print('False')