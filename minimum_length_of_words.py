a=input()
c=[]
for word in a.split():
    c.append(len(word))
print(min(c))