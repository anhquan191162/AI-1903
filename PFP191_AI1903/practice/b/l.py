rows = 7
for i in range(rows):
    for s in range(rows-i-1):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for j in range(i,-1,-1):
        print('*',end='')
    print()
for i in range(rows,1,-1):
    for s in range(rows-i+1):
        print(' ',end='')
    for j in range(i,2*i-1):
        print('*',end='')
    for j in range(1,i-1):
        print('*',end='')
    print()