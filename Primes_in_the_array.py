n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(max(a)+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            if i in a:
                c.append(i)
print(len(c))