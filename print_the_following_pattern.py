rows=int(input())
for i in range(rows,0,-1):
    for j in range(rows,0,-1):
        if i==j:
            print('0',end='')
        else:
            print('x',end='')
    print()