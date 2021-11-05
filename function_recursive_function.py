# Recursive function .
def calc_factorial(x):
    """This is a recursive function to find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        print("Else x:",x)
        return (x * calc_factorial(x-1))
num = 4
print("The factorial of", num, "is", calc_factorial(num))
'''
# First time calling
calc_factorial(4)
- 4==1 NO
   else
       return (4*calc_factorial(4-1))=return (4* calc_factorial(3))#return(4*3*(2*1))
                 -< calc_factorial(3)                                      =4*3*2*1=24
                 -< 3==1 NO
                     else
                        return(3*calc_factorial(2))#return (3*(2*1))
                        -< 2==1 NO
                          else
                             return (2*calc_factorial(1)) # return (2*1)
                              -< 1 == 1 , return 1 
  '''               
