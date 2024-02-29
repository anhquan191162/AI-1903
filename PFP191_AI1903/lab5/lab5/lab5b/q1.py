class Vehicle:

    def __init__(self, name,  max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = 'White'
    
    def seating_capacity(self, capacity):
        return f"The seating capacity of {self.name} is {capacity} passengers"

    def print(self):
        print(f"Vehicle name: {self.name} \nSpeed: {self.max_speed} \nMileage: {self.mileage} \nColor : {self.color}")
        


Vehicle1 = Vehicle('Bus', 240, 18)
Vehicle1.print()

class Vehicle2:
    pass


