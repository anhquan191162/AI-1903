class Students:
    def __init__(self, id, name, gender, age, math, physics, chemistry):
        self.id = id 
        self.name = name
        self.gender = gender 
        self.age = age
        self.math = math
        self.physics = physics
        self.chemistry = chemistry
        self.GPA = 0
        self.rank = ''


class Students_Manager():
    def __init__(self):
        self.students = []
    def incre_id(self):
        maxId = 1
        if len(self.students) > 0:
            maxId = self.students[0].id
            for student in self.students:
                if maxId < student.id:
                    maxId = student.id
                maxId = maxId + 1
        return maxId

    def GPA(self,k : Students):
        unw = float((float(Students.math) + float(Students.physics) + float(Students.chemistry))/3) 
        k.GPA = round(unw)
        
    def rank(self, k : Students):
    
        if k.GPA >= 8:
            Students.rank = 'GIOI'
        elif 6.5 <= k.GPA < 8:
            Students.rank = 'KHA'
        elif 5 <= k.GPA < 6.5:
            k.rank = 'TB'
        elif 0 <= k < 5:
            k.rank = 'YEU'

    def add_students(self, id, name, gender, age, math, physics, chemistry):
        self.students.append(Students(self, id, name, gender, age, math, physics, chemistry))
    def display(self):
        for student in self.students:
            print(f"\nTEN SINH VIEN: {student.name}\nID: {student.id}\nGIOI TINH: {student.gender}\nTUOI TAC: {student.age}\nDIEM TOAN : {student.math}\nDIEM LY: {student.physics}\nDIEM SINH HOC: {student.chemistry}\nDIEM TB: {student.GPA}\nHOC LUC: {student.rank}")
    def delete_students(self,id):
        id = int(input("NHAP ID CUA SINH VIEN MUON XOA: "))
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
            else:
                print("ID KHONG TON TAI.")
    def search_students(self,name):
        name = input("NHAP TEN MUON TIM: ")
        for student in self.students:
            if student.name == name:
                self.display()
            else:
                print("TEN KHONG TON TAI.")
    def GPA_sort(self):
        self.students.sort(key = lambda x : x.GPA, reverse= False)
    def name_sort(self):
        self.students.sort(key = lambda x : x.name, reverse=False)
    def ID_sort(self):
        self.students.sort(key= lambda x : x.id)


    

