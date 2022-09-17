n=int(input())
t=n
rev=0
while n>0:
    sq=t**2#144
    a=str(sq)
    r=n%10
    rev=(rev*10)+r
    n=n//10
sq2=rev**2#441
b=str(sq2)
if a==b[::-1]:
    print('True')
else:
    print('False')