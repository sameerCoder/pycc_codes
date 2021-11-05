# parent class
# Hierarichal inheritance .

class school():

    def schooladdress(self,address):
        self.address=address
        print("parent address",self.address)

class student(school):
    def studentdetail(self,name,roll):
        self.name=name
        self.roll=roll

    def displaystudent(self):
        print("student details:")
        print(self.name)
        print(" school address:",self.address)
#Hierarichal #one parent two child
class teacher(school):
    def getdatateacher(self,teachername):
        self.teachername=teachername
        
    def displayteacher(self):
        print("teacher name:",self.teachername)
        print("teacher school address:",self.address)

#Multilevel inheritant .
class test(student):
    def getdatatest(self,tmarks,name,roll):
        self.tmarks=tmarks
        self.name=name
        self.roll=roll
        print("student name:",self.name)
        print("student roll:",self.roll)
        print("student marks:",self.tmarks)
#class school2():
   # pass
    

#class hybridschool(school2):
  #  pass
    
schooladdress=input("Enter school address:")
roll=int(input("Enter roll number:"))
name=input("Enter name of the student:")
teachername=input("Enter name of the teacher:")
studentmarks=int(input("Enter the marks:"))


t1=teacher()
t1.schooladdress(schooladdress)
t1.getdatateacher(teachername)
t1.displayteacher()

s1=student()
s1.studentdetail(name,roll)
s1.schooladdress(schooladdress)
s1.displaystudent()

t1=test()
t1.getdatatest(studentmarks,name,roll)





    


    
    
