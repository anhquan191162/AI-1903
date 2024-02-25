file_name = "C:\\Users\\admin\\OneDrive\\Tài liệu\\GitHub\\AI-1903\\PFP191_AI1903\\lab4\\story.txt"

count = 0
with open(file_name, 'r') as file:
    content = file.read()
    print(content.split())
    content2 = content.split()
    for i in content2:
        for j in i:
            if j.isupper():
                count = count + 1

print(count)
                 