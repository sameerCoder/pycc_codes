# Exceptional Hirerchy

try :
    print(100/0)
    print("end of try.")

except ArithmeticError:
    print("This is Arithmetic Error.")

except ZeroDivisionError:
    print("This is ZeroDivisionError.")
################################################################
# Default except .

try:
    print(20/0)
except ZeroDivisionError:
    print(" This is zerodivisionerror .")

except :
    print("Some Exception Error ")
    # if ValueError or any other exception occur then this
    # default exception will occur.
    
################################################################
'''    
try:
    print(20/0)

except :
    print("Some Exception Error ")
    # if ValueError or any other exception occur then this
    # default exception will occur.
    
except ZeroDivisionError:
    print(" This is zerodivisionerror .")
'''

'''
Default exception should always be atlast
'''

###############################################
# Finally block.

try:
    print("inside try.")
    print(10/0)
except ZeroDivisionError:
    print("inside exceptional.")

finally:
    print("inside finally.")

#######
    
try:
    print("inside try.")
    print(10/0)
except ValueError:
    print("inside exceptional.")

finally:
    print("inside finally.")

    






    
