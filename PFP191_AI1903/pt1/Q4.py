class Main:
    
    #====================f1====================
    def f1(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        
        inputString = inputString.replace(',', '')
        inputString = inputString.split()
        print(inputString)
            
            
            
        


                
        # end def


    #====================f2====================
    def f2(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        inputString = inputString.replace(',', '')
        inputString = inputString.split()
        pos = [0,0]
        direction_n_distance = inputString
        if direction_n_distance[0].upper() ==  'UP':
                pos[0] += int(direction_n_distance[1])
        elif direction_n_distance[0].upper() == 'DOWN':
                pos[0] -= int(direction_n_distance[1])
        elif direction_n_distance[0].upper() == 'LEFT':
                pos[1] += int(direction_n_distance[1])
        elif direction_n_distance[0].upper() =='RIGHT':
                pos[1] -= int(direction_n_distance[1])
        else:
                pass
        distance = round(float(pos[0])**2) +(float(pos[1]**2))
        print( f"Distance: {distance}")
        # end def

#================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (2 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" Your selection (1 -> 2): ")
        choice = int(input())
        inputString = input()
        print("OUTPUT")
        if choice == 1:
            self.f1(inputString)
        elif choice == 2:
            self.f2(inputString)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()
