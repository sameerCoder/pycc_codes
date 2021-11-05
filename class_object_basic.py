# First class programe.

class student(object):

    studentcount = 0 # is a classs variable whose value is shared among all instances of this class.

    def __init__ (self,rollno,name,course):

      self.rollno=rollno
      self.name=name
      self.course=course
      student.studentcount+=1
     #def __init__():
         
     
    #def getdata(self,rollno,name,course):
       #  self.rollno=rollno
       #  self.name=name
       #  self.course=course


    def displaycount(self):
      
      print( " Total Students :",student.studentcount)


    def displaystudent ( self ):
        #pass
       print ( "Roll no:", self.rollno)
       print ("Name :", self.name)
       print ("Course :",self.course)


#stud1=student()

#stud1=student(10,"tawa","cse")
#stud11=student()
#stud11.getdata(10,"tawa","cse")

stud1=student(10,"Rohan","CSE")

stud2=student(20,"Ram","ECE")
stud3=student(30,"Sam","MECH")

print("Detail of Student 1 >")
stud1.displaycount()
stud1.displaystudent()

print()
#print("Detail of Student 2 >")
stud2.displaycount()
stud2.displaystudent()
print()

print("Detail of Student 3 >")

stud3.displaystudent()

stud3.displaycount()
