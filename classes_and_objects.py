# A class is python is a group of objects
# For example a group of humans
# Where every human is an object
# Every object has properties and methods
# For a human properties are the name,age,gender etc
# Then the methods are sleeps,eats,cries

# creating a class in python
class Human:
    def __init__(self,n,o):# This function initialises the properties of this class. self means the class itself
        self.name=n # Name is a property of the class Human
        self.occupation=o
    
    def do_work(self): # This is a method for the class Human
        if self.occupation=='tennis player':
            print(self.name,'plays tennis')
        elif self.occupation=='actor':
            print(f'{self.name} acts movies')

    def speaks(self):
        print(self.name,'says how are you')

# Creating an instance of the class
# This instance is called an object

tom=Human('tom cruise','actor')
tom.do_work()
tom.speaks()

maria=Human("maria","tennis player")
maria.do_work()
maria.speaks()
        
