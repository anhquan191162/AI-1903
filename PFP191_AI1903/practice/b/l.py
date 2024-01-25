numberofletters = 0
numberofdigits = 0
numberofothers = 0

str1 = str(input("Enter strings: "))

new_str1 = (str1.replace(" ", ""))
numberofletters = len(new_str1)
for i in new_str1:
    if i.isdigit():
        numberofdigits += 1
        numberofletters -= 1

for i in range(0, len(str1)):
    if i == " ":
        numberofothers += 1
    



print(new_str1)
print(numberofothers)
print(numberofdigits)
print(numberofletters)
