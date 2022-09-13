a=input()
c=[]
for word in a.split():
    c.append(len(word))
for i in c:
    print(i,end=' ')