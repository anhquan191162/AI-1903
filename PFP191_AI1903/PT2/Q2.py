import os
__location__ = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))

class Employees():
    def __init__(self,Code,name,salary,allowance):
        self.C = Code
        self.n = name
        self.s = salary
        self.a = allowance
        self.t = salary + allowance
class EmployeeManger():
    def __init__(self):
        self.list = []
    def add(self):
        n = int(input("Enter num of employees: "))
        for i in range(1,n+1):
            print(f'Employee {i}')
            code = (input("Enter code: "))
            name = str(input("Enter name: "))
            salary = float(input("Enter salary: "))
            allowance =float(input("Enter allowance: "))
            
            self.list.append(Employees(code,name,salary,allowance))
        
        with open(os.path.join(__location__,'input.txt'),'w') as file:
            for i,employee in enumerate(self.list):
                file.write(f"Employee {i+1}\nName: {employee.n}\nCode: {employee.C}\nSalary: {employee.s}\nAllowance: {employee.a}")
    def sort_code(self):
        f = int(input("Enter code of an employee: "))
        for emp in self.list:
            if emp.C == f:
                self.list.remove(emp)
    

    def sort_2(self):
        sorted_employees = sorted(self.list, key=lambda x: x.t)
        with open(os.path.join(__location__,'result.txt'),'w') as file:
            for i, employee in enumerate(sorted_employees):
                file.write(f"Employee {i+1}\nName: {employee.n}\nCode: {employee.C}\nSalary: {employee.s}\nAllowance: {employee.a}\n")
                print(f"Employee {i+1}\nName: {employee.n}\nCode: {employee.C}\nSalary: {employee.s}\nAllowance: {employee.a}\n")

key = EmployeeManger()
def Main():
    print("1.Add employee\n2.Remove employee by code\n3.Print list in order\n4.Exit")
    opt = int(input("Enter option: "))
    while opt != 4:
        if opt == 1:
            key.add()
            print()
            Main()
        elif opt == 2:
            key.sort_code()
            print()
            Main()
        elif opt == 3:
            key.sort_2()
            print()
            Main()
        else:
            print("Invalid choice.")
            print()
            
            return Main()
    print("Exiting.")
        

Main()
