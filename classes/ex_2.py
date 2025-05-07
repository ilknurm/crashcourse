# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.
# 
# seating_capacity() a default value of 50.

# Use the following code for your parent Vehicle class.

class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

audi = Vehicle("Audi",240,8)
print(audi.name,audi.max_speed,audi.mileage)

class Bus(Vehicle):
    pass

school_bus = Bus("School Bus",120,101)
print("Vehicle name: ", school_bus.name,school_bus.max_speed,school_bus.mileage)