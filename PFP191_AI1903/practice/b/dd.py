class Students():
    def __init__(self,Name,Class,Assessment,PracticalExam,FinalExam):
        self.n = Name
        self.c = Class
        self.a = Assessment
        self.pe = PracticalExam
        self.fe = FinalExam

class Students_Manager():
    def __init__(self):
        self.students = []
    def add(self,Name,Class,Assessment,PracticeExam,FinalExam):
        self.students.append(Students(Name,Class,Assessment,PracticeExam,FinalExam))
    def display(self):
        for student in self.students:
            print(f"Name: {student.n}\nClass: {S}")