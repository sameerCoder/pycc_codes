class Test: 
    def __init__(self, a, b): 
        self.a = a 
        self.b = b 
  
    def __repr__(self):
        print("repr function called here.")
        return "Test a:%s b:%s" % (self.a, self.b) 
  
# Driver Code         
t = Test(1234, 5678) 
print(t) 
