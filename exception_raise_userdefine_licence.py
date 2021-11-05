# Exception with raise keyword . driving licensce script.

# creating User Defined Exceptional.
# Exceptional Handling Userdefined created.

class Drivingoldage(Exception):
    # New class has been created with classname Drivingoldage
    # Parent class is Exception class.

    def __init__(self,arg):
        # Constructor  created with arg as argument.
        self.msg=arg
        print(self.msg)

class Drivingearlyage(Exception):
    # New class has been created with classname Drivingearlyage
    # Parent class is Exception class.

    def __init__(self,arg):
        # Constructor created with arg as argument.
        self.msg=arg
        print(self.msg)

age=int(input("Enter your age:"))

if age<18:
    raise Drivingearlyage("To Early for Driving license.")
    #raise keyword, calling class with argument value into constructor.
elif age<60:
    print("You are at best age to get Driving license.")
    
else:
    raise Drivingoldage("You are too old to get Driving license.")
