# A Sample class with init method 
class Person: 
    # init method or constructor  
    def __init__(self, name): 
        self.name = name 
    # Sample Method  
    def say_hi(self): 
        print('Hello, my name is', self.name) 
    def say_bye(self):
        print("Bye,",self.name)
    
p = Person('python user ') 
p.say_hi() 
p.say_bye()
