# decorator function.


# below is decorator .


def deco(funarg):
    def inner(name):
        if name=="python":
            print("you are programming language.")
        else:

            funarg(name)
            # else you call function as is it .
    return inner

            
# Below is normal function.

@deco
def printname(name):
    print("Hello ",name)

printname("sam")
printname("ram")
printname("python")
printname("jntu")




    
