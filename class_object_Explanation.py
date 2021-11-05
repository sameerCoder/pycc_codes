# Class and object explanation.

class fruit(object):
    data_variable=10

    def __init__(self,a):
        self.a=a
        print("The name of fruit is :",self.a)

    def memberfunction(self):
        print("Inside class function.")



apple=fruit("apple")
apple.memberfunction()
mango=fruit("mango")
