inputline = str(input("Enter line: ")).lower()
inputline = "".join(inputline.split())
print(inputline)

dict = {}
for char in inputline.replace(" ", ""):
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1
print(dict)

