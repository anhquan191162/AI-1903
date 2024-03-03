def menu():
    print(
        "Menu: "
        "\n1.Report"
        "\n2.Admin"
        "\n3.Exit"
    )
def Report():
    print("1.Class Result")
    print("2.Pupil Report Card")
    print("3.Back to main menu")
def Admin():
    print(
        "Admin Menu\n"
        "1.Create Pupil Record\n"
        "2.Display all Pupil Records\n"
        "3.Search Pupil Record\n"
        "4.Modify Pupil Record\n"
        "5.Delete Pupil Record\n"
        "6.Back To Main Menu"
    )
class Pupil():
    def __init__(self, id, name, english_gr, math_gr, physics_gr, chemistry_gr, CS_gr):
        self.id = id 
        self.name = name
        self.english = english_gr
        self.math = math_gr
        self.physics = physics_gr
        self.chemistry = chemistry_gr
        self.cs = CS_gr
class Pupil_Record_Manager():
    def __init__(self):
        self.pupils = []
    def add_pupils(self, id, name, english_gr, math_gr, physics_gr, chemistry_gr, CS_gr):
        
        self.pupils.append(Pupil(id, name, english_gr, math_gr, physics_gr, chemistry_gr, CS_gr))
        
    def display_pupils(self):
        print("======================")
        print("PUPIL DETAILS...\n")
        for pupil in self.pupils:
            print(f"Roll number: {pupil.id}\nName: {pupil.name}\nEnglish marks: {pupil.english}\nMath marks: {pupil.math}\nPhysics marks: {pupil.physics}\nChemistry marks: {pupil.chemistry}\nCS marks: {pupil.cs} ")
    def search_pupils(self, id):
        for pupil in self.pupils:
            if pupil.id == id:
                return pupil
        return None
    def modify_pupils(self, id):
        for index, pupil in enumerate(self.pupils):
            if pupil.id == id:
                modify_name = input("Want to edit name? (y/n):  ")
                if modify_name.lower() == 'y':
                    self.pupils[index].name = input("Enter new name: ")
                modify_english = input("Want to edit English mark? (y/n):  ")
                if modify_english.lower() == 'y':
                    self.pupils[index].english = float(input("Enter new English mark: "))
                modify_math = input("Want to edit Math mark? (y/n):  ")
                if modify_math.lower() == 'y':
                    self.pupils[index].math = float(input("Enter new Math marks: "))
                modify_physics = input("Want to edit Physics marks? (y/n):  ")
                if modify_physics.lower() == 'y':
                    self.pupils[index].physics = float(input("Enter new Physics marks: "))
                modify_chemistry = input("Want to edit Chemistry marks? (y/n):  ")
                if modify_chemistry.lower() == 'y':
                    self.pupils[index].chemistry = float(input("Enter new Chemistry marks: "))
                modify_CS = input("Want to edit CS marks? (y/n):  ")
                if modify_CS.lower() == 'y':
                    self.pupils[index].CS = float(input("Enter new CS marks: "))
                
        print("Pupil not found.")
    def delete_record(self, id):
        for pupil in self.pupils:
            if pupil.id == id:
                self.pupils.remove(pupil)
        return self.pupils
    def display_record_table(self):
        print(f"{'Roll number'.ljust(5)} {'Name'.ljust(20)} {'English'.rjust(10)} {'Math'.rjust(10)} {'Physics'.rjust(10)} {'Chemistry'.rjust(10)} {'CS'.rjust(10)}")
        for pupil in self.pupils:
            print(f"{str(pupil.id).ljust(5)} {str(pupil.name).ljust(20)} {str(pupil.english).rjust(10)} {str(pupil.math).rjust(10)} {str(pupil.physics).rjust(10)} {str(pupil.chemistry).rjust(10)} {str(pupil.cs).rjust(10)}")
    
            
                
                
        
            

        

menu()
sys = Pupil_Record_Manager()
option = int(input("Enter option: "))


while option !=3:
    if option == 1:
        Report()
        Report_option = int(input("Enter report option: "))
        while Report_option!= 3:
            if Report_option == 1:
                print("CLASS RESULT....")
                sys.display_record_table()
                print()
                print("Done.")
                
                
                break
            elif Report_option == 2:
                id = int(input("Enter the rollno you want to search: "))
                pupil = sys.search_pupils(id)
                if pupil:
                    sys.display_pupils()
                break
            else:
                print("Invalid option.")
                print()
            
        
        print("Returning to menu...")
        print()
        
    elif option == 2:
        Admin()
        admin_option = int(input("Enter admin option(1-6): "))
        while admin_option !=6:
            if admin_option == 1:
                id = int(input("Enter roll number: "))
                name = str(input("Enter name: "))
                english_gr = float(input("Enter marks in English: "))
                math_gr = float(input("Enter marks in math: "))
                physics_gr = float(input("Enter marks in physics: "))
                chemistry_gr = float(input("Enter marks in chemistry: "))
                CS_gr = float(input("Enter marks in CS: "))
                sys.add_pupils(id, name, english_gr, math_gr, physics_gr, chemistry_gr, CS_gr)
                add_more_option = str(input("Do you want to add more?(y/n): ")).lower()
                while add_more_option != 'n':
                    if add_more_option == 'y':
                        id = int(input("Enter roll number: "))
                        name = str(input("Enter name: "))
                        english_gr = float(input("Enter marks in English: "))
                        math_gr = float(input("Enter marks in math: "))
                        physics_gr = float(input("Enter marks in physics: "))
                        chemistry_gr = float(input("Enter marks in chemistry: "))
                        CS_gr = float(input("Enter marks in CS: "))
                        sys.add_pupils(id, name, english_gr, math_gr, physics_gr, chemistry_gr, CS_gr)
                        add_more_option = str(input("Do you want to add more?(y/n): ")).lower()
                    else:
                        print("Invalid choice.")
                        break
                print("Retruning to Admin's menu.....")
                print()
            
            
                
                
            elif admin_option == 2:
                
                    sys.display_pupils()
                    print("Pupil Details Printed.")
                    print("========================")
                    print("Returning to Admin's Menu...")
                
            elif admin_option == 3:
                id = int(input("Enter rollno you want to search : "))
                found_pupil = sys.search_pupils(id)
                print()
                if found_pupil:
                    
                    sys.display_pupils()
                    print()
                else:
                    print("Pupil does not exist.")
                    print("Returning to Admin's Menu...")
            elif admin_option == 4:
                print("Modify Record.")
                id = int(input("Enter roll number: "))
                found_pupil = sys.search_pupils(id)
                if found_pupil:
                    sys.modify_pupils(id)
                    print("Record updated.")
                    print("Printing updated record: ")
                    print()
                    sys.display_pupils()
                    print("Record printed.")
                    print("Returning to Admin's menu....")
            elif admin_option == 5:
                print()
                print("DELETE RECORD.")
                id = int(input("Enter roll number: "))
                print()
                pupil = sys.search_pupils(id)
                if pupil:
                    sys.display_pupils()
                    sys.delete_record(id)
                    print("Record found and deleted")
                print()
                print("Returning to Admin's menu...")
                print()


            else:
                print("Not valid option.")
            print()
            Admin()
            admin_option = int(input("Enter admin option(1-6): "))
        print("Returning to menu...")
        
        
    else:
        print("Invalid choice.")
    print()
    menu()
    option = int(input("Enter option: "))
print("Exiting.")
