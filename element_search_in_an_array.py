n=int(input())
arr=list(map(int,input().split()))
a=int(input())
c=0
for i in range(0,n):
    if arr[i]==a:
        c=1
if c==1:
    print('True')
else:
    print('False')