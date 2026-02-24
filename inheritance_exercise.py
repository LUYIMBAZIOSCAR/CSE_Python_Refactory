class Animal():
    def __init__(self,habitat):
        self.habitat=habitat

    def print_habitat(self):
        print(self.habitat)    

    def sound(self):
        print("Some Animal Sound")

class Dog(Animal):
    def __init__(self):
        super().__init__("Kennel")

    def sound(self):
        print("Woof Woof ")

dog2=Dog()
dog2.print_habitat()
dog2.sound()






