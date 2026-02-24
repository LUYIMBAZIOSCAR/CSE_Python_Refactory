class Vehicle:
    def general_usage(self):
        print("general use: transportation")

# Deriving my sub class of car of the class of Vehicle
# The class Vehicle is the class and car and motorcycle are its children
# The child inherits all properties and methods from the parent
class Car(Vehicle):
    def __init__(self):
        print("I'm car")
        self.wheels=4
        self.has_roof=True

    def specific_usage(self):
        print("Specific use: commute to work,vacation with family")

class Motorcycle(Vehicle):
    def __init__(self):
        print("I'm motorcycle")
        self.wheels=4
        self.has_roof=True

    def specific_usage(self):
        print('specific use: road trip, racing')

c=Car()
c.general_usage()
c.specific_usage()

m=Motorcycle()
m.general_usage()
m.specific_usage()
# I can call a property or a method from my parent class
# using an object of the child class