# Basic class progrma

class student():

    '''
This is student class .
'''
    variable1=10 
    def getdata(self,rollno,name):
        self.rollno=rollno
        self.name=name

    def display(self):
        print("Display the data of student:")
        print("Roll :",self.rollno,"name:",self.name)
        

class school(student):

        variable2=20
        def schoolfunction():
            #pass
            print(variable1)


    
stud1=student()
stud1.getdata(1,"Avinash")
stud1.display()

stud2=student()
stud2.getdata(2,"Ravi")
stud2.display()

school1=school()
school1.getdata(3,"Tamuka")
school1.display()

