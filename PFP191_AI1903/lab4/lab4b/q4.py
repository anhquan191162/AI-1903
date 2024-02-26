import os
import shutil
newfile1 = 'matter.txt'
file5 = "C:\\Users\\admin\\OneDrive\\Tài liệu\\GitHub\\AI-1903\\PFP191_AI1903\\lab4\\poem.txt"
with open(newfile1, 'w+') as file:
    file.write("THE WORLD IS ROUND")
path = "C:\\Users\\admin\\OneDrive\\Tài liệu\\GitHub\\AI-1903\\PFP191_AI1903\\lab4"
'''shutil.move(newfile1, path)'''


def hash_display(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        for letter in content:
            print(letter, end='#')

hash_display(file5)

print("\n====================")

newfile2 = 'WORDS.txt'
with open(newfile2, 'w+') as file:
    file.write("WELL, THJS JS A WORD BY JTSELF. YOU COULD STRETCH THJS TO BE A SENTENCE")

'''shutil.move(newfile2, path)'''
def JTOI(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        for i in content:
            if i == 'J':
                print('I', end='')
            else:
                print(i, end='')
        
JTOI(newfile2)


