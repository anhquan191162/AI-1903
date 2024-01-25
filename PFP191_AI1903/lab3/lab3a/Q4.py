string = str(input("Enter string: "))
new_string = ""
for i in string:
    if i.isdigit():
        new_string = new_string + i
print(new_string)


string2 = str(input("Enter string: "))
new_string2 = ''.join(char for char in string2 if char.isalnum())
print(new_string2)

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
clear_list = []
for char in str_list:
    if char != None :
        clear_list.append(char)
while "" in clear_list:
    clear_list.remove("")

        



print(str(clear_list))



str1 = 'Emma-is-a-data-scientist'
str1 = str1.split('-')

for i in str1:
    print(i)