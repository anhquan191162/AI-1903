import os

'''print(os.listdir('C:\\Users\\admin\\OneDrive\\Tài liệu\\GitHub\\AI-1903\\PFP191_AI1903\\'))'''

L = [
    "Mot cay lam chang nen non",
    "\nBa cay chum lai nen hon nui cao"
]
file1 = "C:\\Users\\admin\\OneDrive\\Tài liệu\\GitHub\\AI-1903\\PFP191_AI1903\\poem.txt"
with open("C:\\Users\\admin\\OneDrive\\Tài liệu\\GitHub\\AI-1903\\PFP191_AI1903\\poem.txt", 'w') as file:
    file.writelines(L)


def readlines(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file.readlines():
                print(line.strip())

readlines(file1)

print("======================")

file2 = 'story.txt'
L2 = [
    "A boy is playing there.",
    "\nThere is a playgroud.",
    "\nAn airplane is in the sky.",
    "\nThe sky is pink.",
    "\nAlphabets and numbers are allowed in the password."
]
with open(file2, 'w+') as file:
    file.writelines(L2)
current_directory = os.path.dirname(os.path.abspath(__file__))
newpath = os.path.join(file2, current_directory)

def counting_lines(file_name):
    count = 0
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            
            for i in file:
                for j in i[0]:
                    if j == 'T':
                        count += 1
                else:
                    pass
                
            
    return count



       
           
with open(file2) as file:
    total_lines = len(file.readlines())
    sum = total_lines - counting_lines(file2)
    print(f"Total of lines that does not starts with 'T': {sum}")






        
