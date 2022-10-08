n=input()
count=0
for i in n:
    if i.isalpha() or i==' ' :
        pass
    else:
        count+=1
print(count)