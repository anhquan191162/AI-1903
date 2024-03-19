str = 'papa'
newstr = ''
for i in str:
    if i == 'p':
        i = 'm'
    newstr += i
print(newstr)