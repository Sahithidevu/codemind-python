n=int(input())
arr=list(map(int,input().split()))
lst=[]
for i in range(len(arr)):
    if arr[i]%2==0:
        lst.append(arr[i])
lst.reverse()
print(lst[0])