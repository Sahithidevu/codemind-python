a=input()
n=a.split()
c=[]
for i in range(len(n)):
    rev=n[i][::-1]
    c.append(rev)
c.reverse()
print(*c)