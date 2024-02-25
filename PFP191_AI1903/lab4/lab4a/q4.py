import os 
import shutil
import datetime

current_directory = os.path.dirname(os.path.abspath(__file__))
file1 = "C:\\Users\\admin\\OneDrive\\Tài liệu\\GitHub\\AI-1903\\PFP191_AI1903\\renamed_sales.txt"
file2 = "C:\\Users\\admin\\OneDrive\\Tài liệu\\GitHub\\AI-1903\\PFP191_AI1903\\poem.txt"
def rename_file(old_file, new_file):
    if os.path.exists(old_file):
        os.rename(old_file, new_file)
        print(f"All files renamed: {file1} to {file2} ")
    else:
        print("Non-existant file.")
    
rename_file(file1, file2)

def rename_multiple_files(files, new_names):
    if len(files) != len(new_names):
        print("Not enough input.")
        return
    for i in range(len(files)):
        rename_file(files[i], new_names[i])

files = ["new_file_2.txt", "sample.txt"]
new_names = ["renamed_file_2.txt", "new_sample.txt"]
rename_multiple_files(files, new_names)

def rename_files_in_folder(folder_path, files, new_file_name):
    os.chdir(folder_path)
    rename_multiple_files(files, new_file_name)

rename_files_in_folder("C:\\Users\\admin\\OneDrive\\Tài liệu\\GitHub\\AI-1903\\PFP191_AI1903", new_names, files)

def rename_w_time(fil_name):
    time = datetime.datetime.now().strftime("%d-%m-%Y")
    name , ext = os.path.splitext(fil_name)
    new_name = f"{name}_{ext}"
    rename_file(fil_name, new_name)

rename_w_time("C:\\Users\\admin\\OneDrive\\Tài liệu\\GitHub\\AI-1903\\PFP191_AI1903\\newfile3.txt")

def change_extension(file_name, new_extension):
    base_name, _ = os.path.splitext(file_name)
    new_name = f"{base_name}.{new_extension}"
    rename_file(file_name, new_name)


def rename_and_move_file(old_path, new_path):
    shutil.move(old_path, new_path)
    print(f"File moved from '{old_path}' to '{new_path}'.")