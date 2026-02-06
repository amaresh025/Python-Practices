class Class:
    #without constructor 
    def hello(self, name, rollno):
        self.name = name
        self.rollno = rollno
    
    def show(self):
        print(self.name, self.rollno)
        
student = Class()
student.hello("Baby", 54)
student.show()