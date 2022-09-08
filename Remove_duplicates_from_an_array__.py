n=int(input())
arr=list(map(int,input().split()))
d=[]
for i in range(n):
    if arr[i] in d:
        continue
    else:
        d.append(arr[i])

for i in range(len(d)):
    print(d[i],end=' ')