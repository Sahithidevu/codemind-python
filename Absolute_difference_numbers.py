a,b=map(int,input().split())
tmp=10**(b)
x=a%tmp
tmp1=int(str(a)[::-1])
y=tmp1%tmp
y=int(str(y)[::-1])
print(abs(x-y))