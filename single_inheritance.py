# Single level Inheritance .

class student(object):

  def getData(self,roll,name):

    self.roll=roll
    self.name=name


  def displaystudent(self):
    print("")
    print("parent roll:",self.roll)
    print("parent name :",self.name)


# Single Inheritance Derive Class.

class Test(student):

  def getmarks(self,marks):

    self.marks=marks

  def displaymarks(self):
    print("child class method calling .")
    print("Roll No;",self.roll)
    print("Name :",self.name)
    print("Total Marks:",self.marks)
    

r=int(input (" Enter Roll:"))
n=input("Enter name :")
m=int(input("Enter marks :"))


#creating Object .
# objectname=clasname
t1=Test()
t1.getData(r,n)
t1.getmarks(m)
t1.displaystudent()
t1.displaymarks()











    
