# Basic plus class progrma

class student():

    '''
This is student class .
'''
    variable1=10 
    def getdata(self,rollno,name):
        self.rollno=rollno
        self.name=name
        #vari=29 # ERROR will come as vari is not define inside class,not allowed inside function.
        #print(self.vari)
        print("self.variable+1",self.variable1+1)
       
        print("print inside getdata function:",stud1.name)
        print("print inside getdata function:",self.name)

    def display(self):
        print("Display the data of student:")
        print("Roll :",self.rollno,"name:",self.name)


stud1=student()
print("stud1.variable1:",stud1.variable1)
stud1.getdata(1,"Avinash")
stud1.display()

stud2=student()
stud2.getdata(2,"Ravi")
stud2.display()

stud3=student()
stud3.getdata(3,"pythonstudent")
stud3.display()
