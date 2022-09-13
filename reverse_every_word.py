a=input()
c=[]
for word in a.split():
    c.append(word[::-1])
print(*c)