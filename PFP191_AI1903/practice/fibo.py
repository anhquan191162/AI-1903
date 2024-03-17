class Students:
    def __init__(self,name,age,mark):
        self.name = name
        self.age = age
        self.mark = mark
    
def sort_key(Students):
    return Students.name

students = []

while True:
    num_of_stu = input("Enter number of students: ")
    if num_of_stu.isdigit():
        break
    else:
        print("Please enter a number")
for i in range(int(num_of_stu)):
    temp = int(input("Enter student : "))
    students.append(Students(
        input("Enter name: "),
        int(input("Enter age: ")),
        int(input("Enter mark: ")),
        ))

print('before sorting')
for i in range(len(students)):
    print("Students ",i + 1)
    print("Name: {}\nAge: {}\nMark: {}".format(students[i].name, students[i].age,students[i].mark))
    
print('after sorting')
students.sort(key = sort_key, reverse = False)
for i in range(len(students)):
    print("Students ",i+1)
    print("Name: {}\nAge: {}\nMark: {}".format(students[i].name, students[i].age,students[i].mark))
    