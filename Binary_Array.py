n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(len(a)):
    if a[i]==1 or a[i]==0:
        c=True
    else:
        c=False
if c==True:
    print(True)
else:
    print(False)
    