class Students:
    def __init__(self, id, name, gender, age, math, physics, chemistry):
        self.id = id 
        self.name = name
        self.gender = gender 
        self.age = age
        self.math = math
        self.physics = physics
        self.chemistry = chemistry
    def avg_rank(self):
        rank = ''
        sum = (float(self.math + self.physics + self.chemistry)/3)
        if 0 <= sum <= 10:
            if 8 <= sum < 10:
                rank = 'Gioi'
            elif 6.5<= sum < 8:
                rank = 'Kha'
            elif 5 <= sum < 6.5:
                rank = 'TB'
            else: 
                rank = 'Yeu'
        else:
            print("Invalid.")
                
        return f"GPA : {sum:.2f}, Hoc luc {rank}"

class Students_Manager():
    def __init__(self):
        self.students = []
    def add_students(self, id, name, gender, age, math, physics, chemistry):
        self.students.append(Students(self, id, name, gender, age, math, physics, chemistry))
    def modify_students(self, id):
        pass
        

