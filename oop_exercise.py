class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    
    def do_work(self):
        if self.name=='coder':
            print("This guy builds systems")
        elif self.name=='manager':
            print("This guy is useless")
        else:
            print("This guy is a time waster")
    
    def id_purpose(self):
        if self.id==1:
            print("This guy is first")
        elif self.id==2:
            print("This guy is second")
        else:
            print("you have no position in this company")

# Creating objects
Oscar=Employee(1,'coder')
Oscar.do_work()
Oscar.id_purpose()
Kintu=Employee(2,'manager')
Kintu.do_work()
Kintu.id_purpose()
Mponye=Employee(3,'cleaner')
Mponye.do_work()
Mponye.id_purpose() 

# Creating class car with brand and price
# In this case,brand and price are the properties

class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def brand_do(self):
        if self.brand=='Toyota':
            print("Oli mufuna mpola")
        elif self.brand=='Subaru':
            print("Oli wakabi man")
        else:
            print("High class")

    def price_do(self):
        if self.price<1000:
            print("Oli mwavu")
        else:
            print("Kyakabi gwe musaja")

toyota=Car('Toyota',1000)
toyota.brand_do()
toyota.price_do()

subaru=Car('Subaru',500)
subaru.brand_do()
subaru.price_do()

benz=Car('benz',2000)
benz.brand_do()
benz.price_do()

# Creating a class rectangle to calculate area
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self): # method for calculating area
        area=self.length*self.width
        print(area)

rectangle_1=Rectangle(20,30)
rectangle_1.calculate_area()

# Creating class student with name and marks
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def grade_student(self):
        if self.marks<60:
            print("You are a failure")
        else:
            print("You have passed")

student1=Student("Oscar",30)
print(f'Name:{student1.name}')
print(f'Marks:{student1.marks}')
student1.grade_student()

# Craeting class Person with greeting method
class Person:
    def __init__(self,name):
        self.name=name
    
    def greeting(self): # method for greeting
        print(f'Good morning {self.name}, how are you ')

person1=Person('Oscar')
person1.greeting()

# Creating bank account class with deposit function
class Bank_account:
    def __init__(self,deposit):
        self.deposit=deposit
    def deposit_money(self):
        if self.deposit<1000:
            print('You are very poor')
        else:
            print("Thank you")

account1=Bank_account(4000)
account1.deposit_money()
        
        
        
        


                