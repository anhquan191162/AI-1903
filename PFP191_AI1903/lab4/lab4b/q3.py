import os
file5 = "C:\\Users\\admin\\OneDrive\\Tài liệu\\GitHub\\AI-1903\\PFP191_AI1903\\lab4\\poem.txt"
file4 = "C:\\Users\\admin\\OneDrive\\Tài liệu\\GitHub\\AI-1903\\PFP191_AI1903\\lab4\\story.txt"
def count_uppercase(file_name):
    count = 0
    with open(file_name, 'r') as file:
    
        content = file.read()
        print(content)
        content2 = content.split()
        for i in content2:
            for j in i:
                if j.isupper():
                    count += 1
    return count

print(f"Num of uppercase char: {count_uppercase(file5)}")
print(f"Num of uppercase char: {count_uppercase(file4)}")

