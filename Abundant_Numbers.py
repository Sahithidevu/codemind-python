num=int(input())
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
    else:
        pass
if sum>num:
    print('True')
else:
    print('False')