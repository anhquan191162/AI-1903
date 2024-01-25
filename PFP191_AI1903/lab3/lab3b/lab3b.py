str1 = str(input("Enter string: "))
str2 = str(input("Enter another string: "))
str1_clean =''.join(char.lower() for char in str1 if char.isalnum())
str2_clean = ''.join(char.lower() for char in str2 if char.isalnum())
print(sorted(str1_clean))
print(sorted(str2_clean))
if sorted(str1_clean) == sorted(str2_clean):
    print(f"{str1} is an anargram of {str2}")
else:
    print(f"{str1} is not an anargram of {str2}")






def hexa_check(string):
    try:
        int(string, 16)
        return True
    except ValueError:
        return False
    
str3 = str(input("Enter string:"))

if hexa_check(str3):
    decimal_res = int(str3, 16)
    print(decimal_res)
else:
    print("Error")

    