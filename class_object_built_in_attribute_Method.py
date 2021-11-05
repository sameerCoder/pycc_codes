# Method built in attribute .

class student :
    '''
class documentation
'''
    def __init__ (self,rollno,name,course):

      self.rollno=rollno
      self.name=name
      self.course=course
    def displayStudent(self):
       print("Roll no:",self.rollno)
       print("Name:",self.name)
       print("Course:",self.course)
      
#stud1=student()
#stud1.getdata(10,"Jack","MS")

stud1=student(10,"Jack","MS")
stud1.displayStudent()

at=getattr(stud1,'name')
rn=getattr(stud1,'rollno')
print("getattr(stud1,'name') :",at)
print("getattr(stud1,'rollno') :",rn)


#print("hasattr(stud1,age):",hasattr(stud1,'age'))#python 2 version

##### New attribute .
print("setattr(stud1,age,21):",setattr(stud1,'age',21))
print(" After using Set attribute ")
stud1.displayStudent()
print("Age :",stud1.age)

### Attribute Age deleted .
print("delatrr(stud1,age:)",delattr(stud1,'age'))
print("After del attibute .")
stud1.displayStudent()
print("Age :",stud1.age)
print("End of Programe.")



