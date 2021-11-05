#######################
# Programe to show Built in Attribute of Class. 

class student(object):
    
    "Common   base class fo all students."
    def __init__ (self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def displayStudent(self):
        print("Roll no:",self.rollno)
        print("Name:",self.name)
        print("Course:",self.course)

stud1=student(10,"Jack","MS")
stud1.displayStudent()

print("Student.__doc__:",student.__doc__)
print("student.__name__:",student.__name__)
print("student.__module__:",student.__module__)
print("student.__base__:",student.__base__)
print("student.__dict__:",student.__dict__)
