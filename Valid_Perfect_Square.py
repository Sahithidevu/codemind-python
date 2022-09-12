n=int(input())
for i in range(n):
    a=int(input())
    temp=a**(0.5)
    if temp//1==temp:
        print('True')
    else:
        print('False')