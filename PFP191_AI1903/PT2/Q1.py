def replace(inputStr):
    
    i1 = input()
    i2 = input()
    newstr = ''
    
    for i in inputStr:
        if i == str(i1):
            i = str(i2)
        newstr += i
    return newstr

inputStr = input()
print(replace(inputStr))