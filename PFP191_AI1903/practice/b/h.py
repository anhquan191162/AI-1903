rows = 7
for i in range(rows):
    for j in range(rows-i):
        print(end=' ')
    for k in range(2*i + 1):
        if k == 0:
            print('*',end='')
        elif k == 2*i:
            print('*',end='')
        elif i == rows - 1:
            print('*',end='')
        else:
            print(end=' ')
    

    print()

for i in range(1,rows+1):
    for j in range(i):
        print(end=' ')
    for j in range(1,(rows*2 - (2*i-1)+1)):
        if i == 1 or j == 1 or j == rows*2 - (2*i-1):
            print('*',end='')
        else:
            print(end=' ')
    print()
