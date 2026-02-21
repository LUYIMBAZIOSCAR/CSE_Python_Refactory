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
        