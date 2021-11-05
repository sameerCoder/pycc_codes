# Built in Class Attribute .


class student:
    "Common base class for all students ."

    studentcount = 0 # is a classs variable whose value is shared among all instances of this class.

    def __init__ (self,rollno,name,course):

      self.rollno=rollno
      self.name=name
      self.course=course
      student.studentcount+=1



    def displaycount(self):
      print( " Total Students :",student.studentcount)


    def displaystudent ( self ):
        #pass
       print ( "Roll no:", self.rollno)
       print ("Name :", self.name)
       print ("Course :",self.course)

stud1=student(10,"Rohan","CSE")
stud2=student(20,"Ram","ECE")
stud3=student(30,"Sam","MECH")

print(" student.__doc__:",student.__doc__)
print("student.__name__:",student.__name__)
print("student.__module__:",student.__module__)
print("student.__bases__:",student.__bases__)
print("student.__dict__:",student.__dict__)
print("End")





























      
