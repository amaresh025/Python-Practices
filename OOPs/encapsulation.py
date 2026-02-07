class Class:
    def __init__(self, name, roll_no, std):
        self.name = name
        self.set_rollno(roll_no)
        self.std = std

    def set_rollno(self, roll_no):
        if roll_no < 0:
            raise ValueError ("invalid")
        self._roll_no = roll_no

    def get_rollno(self):
        return self._roll_no
    
get_student = Class("Yash", 74, 10)
print(get_student.get_rollno())