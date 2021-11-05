# Self explanation.


class classname(object):

    def __init__(self,name):

        self.name=name
        # Self is acting as a replacement of object name.
        #self.name=object1.name

    def display(self):
        print("Name of the person is :",self.name)
        print("object name:",object1.name)


object1=classname("Bucky")
object2=classname("ford")

object1.display()
object2.display()
    
