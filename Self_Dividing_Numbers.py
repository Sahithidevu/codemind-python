a=int(input())
b=int(input())
c=[]
for i in range(a,b+1):
    if i>0:
        d=i
        count=0
        while d:
            r=d%10
            if r:
                if i%r==0:
                    count+=1
            d//=10
        if len(str(i))==count:
            c.append(i)
print(*c)
            