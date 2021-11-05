
# To show member variable can be use with help of object only.
class Classname(object):
    data_variable=90 # This is wch attribute ?
    #print(data_variable)

    def function1():
        print("member method/ member function.")



object1=Classname()
object1.function1

#print(data_variable)
print(object1.data_variable)
    
