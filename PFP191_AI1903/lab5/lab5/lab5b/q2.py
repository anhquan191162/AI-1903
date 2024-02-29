from q1 import Vehicle

class Bus(Vehicle):
    pass

bus1 = Bus('School Volvo', 180, 12)
bus1.print()
print(bus1.seating_capacity(50))