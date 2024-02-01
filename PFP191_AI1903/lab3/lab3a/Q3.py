def mixed_string(string):
    middle_len = len(string) // 2
    middle_four = string[middle_len - 2 : middle_len + 2]
    mixed_str =  middle_four
    return mixed_str


str1 = str(input("Enter string: "))
res = mixed_string(str1)
print(f"Original string: {str1}")
print(f"Middle four are: {res}")



def appen_str(string1, string2):
    mid_len = len(string1) // 2
    string3 = string1[:mid_len] + string2 + string1[mid_len:]
    return string3

str1 = 'ab'
str2 = 'cd'
res = appen_str(str1, str2)
print(res)



def mixed_str_create(string1, string2):
    mid_len_string1 = len(string1)// 2
    mid_len_string2 = len(string2)// 2
    mixed_str1n2 = string1[0] + string2[0] + string1[mid_len_string1] + string2[mid_len_string2] + string1[-1] + string2[-1]
    return mixed_str1n2



str1 = 'America'
str2 = 'Japan'
res_mixed = mixed_str_create(str1, str2)
print(res_mixed)



new_str_lower = ''
new_str_upper = ''
new_str =''
string1 = str(input("Enter string: "))
for char in string1:
    if char == char.lower():
        new_str_lower = new_str_lower + char
        
    if char == char.upper():
        new_str_upper = new_str_upper + char
    new_str = new_str_lower + new_str_upper    
print(new_str)
    
        
            
string = str(input("Enter string: "))
new_string = string.replace(" ", "")
spc_count = 0
int_count = 0
nrm_count = 0

for char in string:
    if char.isalnum() == False:
        spc_count +=1
print(f"Total special symbols : {spc_count}")

for i in string:
    number_lis = '0123456789'
    if i in number_lis:
        int_count +=1
print(f"Total intergers: {int_count}")

nrm_count = nrm_count + len(string) - int_count - spc_count
print(f"Total chars: {nrm_count}")



    

