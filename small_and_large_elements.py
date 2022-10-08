n=input()
c=''
for i in n.split(' '):
    c+=(n[::-1])
    m1=min(i)
    break
for i in c.split(' '):
    m2=max(i)
    break
print(m1,m2)