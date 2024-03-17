rows = 6
for i in range(rows):
    for j in range(rows-i-1):
        print(end=' ')
    for k in range(i):
        print(chr(65+k),end='')
    for k in range(i,-1,-1):
        print(chr(65+k),end='')
    print()


string = 'BITTER SPICE ALE MONEY HELLO BYE BITTER BITTER SPICE ALE ALE ALE ALE MONEY MONEY HELLO BYE'


counted_dict = {}
for i in string.split():
    if i not in counted_dict:
        counted_dict[i] = 1
    else:
        counted_dict[i] += 1

print(counted_dict)


