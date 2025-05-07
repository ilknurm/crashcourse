# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
modelx = Vehicle("Audi",240,18)
print(modelx.max_speed, modelx.mileage)

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo",180,12)
print("Vehicle name", School_bus.name, "Speed",School_bus.max_speed,"Mileage",School_bus.mileage)