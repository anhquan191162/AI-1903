import os

file5 = "C:\\Users\\admin\\OneDrive\\Tài liệu\\GitHub\\AI-1903\\PFP191_AI1903\\lab4\\poem.txt"
current_direct = os.path.dirname(os.path.abspath(__file__))

def count_words(file_name):
    
    
    with open(file_name, 'r') as file:
        print(len(file.read().split()))
count_words(file5)  
print("=====================")


def display_words(file_name):
    with open(file_name, 'r') as file:
        content = file.read().split()
        for i in content:
            if len(i) >= 4:
                content.remove(i)
        return content
print(display_words(file5))