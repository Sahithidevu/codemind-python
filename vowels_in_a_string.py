n=input()
a=input()
if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
    print('True')
    for i in range(len(n)):
        if a==n[i]:
            print(i)
            break
else:
    print('False')