# creating class and object.
'''
class classname():
    variable1=10

    def function1ofclass(self):
        print("function inside class")

object1=classname()
print("calling variable of class:",object1.variable1)
print("calling function of class:",object1.function1ofclass())

object2=classname()
print("calling variable of class:",object2.variable1)
print("calling function of class:",object2.function1ofclass())
'''
'''
#with argument in fucntion .
class classname():
    variable1=10

    def function1ofclass(self,a):
        self.a=a
        # object1.10
        # object2.11
        print("function inside class")
        print("a value inside function class:",self.a)

object1=classname()
print("calling variable of class:",object1.variable1)
print("calling function of class:",object1.function1ofclass(10))

object2=classname()
print("calling variable of class:",object2.variable1)
print("calling function of class:",object2.function1ofclass(11))
'''

# class with 2 argument in function .
# create a class of student having argument as name , roll.
# then you have store 2 student data.

class Student(object):
    def studentbehaviour(self,name,roll):
        self.name=name
        self.roll=roll

        print("Name of student:",self.name)
        print("Roll of student:",self.roll)

student1=Student()
student1.studentbehaviour("student1",1)
student2=Student()
student2.studentbehaviour("student2",2)



        



    
    
    















