t=int(input())
for k in range(t):
    n=int(input())
    a=n
    while 1:
        flag=False
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                flag=True
                break
        if flag==False:
            break
        else:
            a+=1
    b=n
    while 1:
        flag=False
        for i in range(2,int(b**0.5)+1):
            if b%i==0:
                flag=True
                break
        if flag==False:
            break
        else:
            b-=1
    if n-b<=a-n:
        print(b)
    else:
        print(a)