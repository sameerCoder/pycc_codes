# First class programe.

class student:

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

#print("Detail of Student 1 >")
#stud1.displaycount()
#stud1.displaystudent()

#print()
#print("Detail of Student 2 >")
#stud2.displaycount()
#stud2.displaystudent()
#print()

#print("Detail of Student 3 >")

#stud3.displaystudent()

#stud3.displaycount()

############ Level 2 Built in Attribute

at = getattr ( stud1 , "name")
print ( "getattr ( stud1 , name ):" , at )

at2=getattr(stud2, "name")
print ("student 2 name :",at2)

#print ( "hasattr(stud1,age):", hasattr(stud1,'age'))

# New attribute inserted .
print ( "setattr (stud1,age,21):",setattr(stud1, 'age' ,21))
print("Display attribute value after inserting new attribute .")
stud1.displaystudent()

print("Age:",stud1.age)


# Attribute Deletion .
print ( "delattr (stud1,age):", delattr(stud1,'age'))
stud1.displaystudent()












































