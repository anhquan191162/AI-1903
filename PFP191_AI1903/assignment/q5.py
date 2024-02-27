inputline = str(input("Enter line: ")).lower()
print(inputline, "\n")

dict = {}
for char in inputline:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1
print(dict)