n=int(input())
a=''
for i in range(n):
    a=''
    for j in range(n):
        if(i==j)or (i+j)==n-1:a+='x'
        else:a+='0'
    print(a)