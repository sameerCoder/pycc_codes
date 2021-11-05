# Class destructor in python .
'''
python automatically delete an object that is  no longer in use.

'''
class student():
  '''
    Hello Class 
'''
  variable1=30
  def __init__(self,rollno,name,course):

    self.rollno=rollno
    self.name=name
    self.course=course

 # def getdata(self,rollno,name,course):
 #   self.rollno=rollno
 #   self.name=name
 #   self.course=course


  def displaystudent(self):

    print ("Roll number :",self.rollno)
    print ("Name :",self.name)
    print ("Course :",self.course)

  def __del__(self):

    #class_name=self.__class__.__name__
    class_name=student.__name__
    print(class_name,"class object got destroyed after calling del method .")
    

stud1=student(200,"Jack","MS")
#stud1=student()
#stud1.getdata(200,"Jack","MS")
stud1.displaystudent()
stud2=student(300,"mack","MSC")
stud2.displaystudent()

del stud1
print("After deleting only stud1 object.")
stud2.displaystudent()
stud1.displaystudent()


  
