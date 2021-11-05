# Decorator chaining.


def dec1(fun):
    def inner(name):
        print("This is decorator1")
        fun(name)

    return inner

def dec2(fun):
    def inner(name):
        print("This is decorator2")
        fun(name)
    return inner

@dec2 # As we have linked decorator2 first , so first decorator2 will be called.
@dec1 # As we have linked decorator1 next line , so after decorator2 , decorator1 will be called.

def studentname(name):
    print("Hello",name,"Good.")

studentname("Python")
# And at last normal function will print the output.
        
