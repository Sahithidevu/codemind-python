a=input()
a=a.lower()
lst=[]
for word in a.split():
    if word==word[::-1]:
        lst.append(word)
print(len(lst))