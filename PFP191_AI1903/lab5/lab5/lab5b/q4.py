class Vehicle3:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus3(Vehicle3):
    pass

School_bus3 = Bus3("School Volvo", 12, 50)
print(type(School_bus3))


print(isinstance(School_bus3, Vehicle3))