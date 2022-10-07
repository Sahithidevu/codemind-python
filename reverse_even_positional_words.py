n=input()
a=n.split()
c=[]
for i in range(len(a)):
    if i%2==0:
        rev=a[i][::-1]
        c.append(rev)
    else:
        c.append(a[i])
print(*c)