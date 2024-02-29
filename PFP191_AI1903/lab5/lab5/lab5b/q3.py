from q1 import Vehicle


class Car(Vehicle):
    pass

Car1 = Car('White Audi', 240, 18)
Car1.print()




class Vehicle2:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity *100
    

class Bus2(Vehicle2):
    
    def fare(self):
        return self.capacity * 100 + int((self.capacity*100)*(10/100))




School_Bus = Bus2("School Volvo", 12, 50)
print(f"Total Bus fare is: {School_Bus.fare()} ")

