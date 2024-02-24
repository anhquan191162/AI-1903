import os 
from datetime import datetime

current_directory = os.path.dirname(os.path.abspath(__file__))

file_name = 'sales.txt'

file_path = os.path.join(current_directory, file_name)

with open('sales.txt', 'w') as file:
    pass
print("sales.txt created.")

current_datetime = datetime.now()
datetime_str = current_datetime.strftime("%d-%m-%Y_%H-%M-%S")
file_name2 = f"{datetime_str}.txt"

file_path2 = os.path.join(current_directory, file_name2)

with open(file_name2, 'w') as file:
    pass
print(f"created {file_name2} ")

permission_file = "sample.txt"
file_path3 = os.path.join(current_directory, permission_file)
with open(permission_file, 'w') as file:
    file.write("File has custom permission.")
    
os.chmod(permission_file, 0o600)
print(f"created {permission_file}.")


new_file = "new_file.txt"

new_file_path = os.path.join(current_directory, new_file)

with open(new_file, 'w') as file:
    file.write(
        "Done writting."
        "\nThis is new content."
    )
with open(new_file, 'r') as file:
    content = file.read()
   

print(content)

with open(new_file, 'w') as file:
    file.write("This is overwritten content.")

with open(new_file, 'r') as file:
    content = file.read()

print(content)

lines = {
    "Name" : "Emma.",
    "Address" : "221 Baker Street.",
    "City" : "London."

}
new_file2 = 'new_file_2.txt'

new_file_path_2 = os.path.join(current_directory, new_file2)
with open(new_file2, 'w') as file:
    for i, j in lines.items():
        file.write(f"{i}, {j}")
        file.write("\n")

with open(new_file2, 'r') as file:
    content = file.read()

print(content)
print("===================")
new_file3 = 'newfile3.txt'

new_file_path_3 = os.path.join(current_directory, new_file3)

with open(new_file3, 'w') as file:
    file.write(
        "My First line."
        "\nMy Second line."
    )
print("==================")
with open(new_file3, 'r+' ) as file:
    file.seek(0)
    print(file.read())
    file.seek(0)
print("================")
with open(new_file3, 'a+') as file:
    file.seek(0,2)
    file.write("\nThis content is added to the end of the file.")

    

with open(new_file3, 'r') as file:
    print(file.read())

print("===============")

with open(new_file3, 'r+') as file:
    file.seek(3, 0)
    print("Current position: ", file.read(5))
    file.seek(19,0)
    print("Current position: ", file.read(6))

print("=============")
with open(new_file3, 'r') as file:
    print(file.read())

with open("C:\\Users\\admin\\OneDrive\\Tài liệu\\GitHub\\AI-1903\\PFP191_AI1903\\newfile3.txt", 'rb+') as file:
    
    file.seek(0)
    x = file.read(8).split()
    print(x)
    print(x[::-1])
    
with open("C:\\Users\\admin\\OneDrive\\Tài liệu\\GitHub\\AI-1903\\PFP191_AI1903\\newfile3.txt","r+") as file:
    print(file.tell())
    print("Printing file content: ","\n",file.read())
    print("File handle at: ", file.tell())
