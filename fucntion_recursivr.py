# Recursive function .

def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))
#5
num = 5
print("The factorial of", num, "is", calc_factorial(num))



'''
# First Else part working..
return 4* calc_factorial(3)
return 3*calc_factorial(2)
return 2*calc_factorial(1)

return 4*3*2*1=24
calc_factorial(3)=3*2*1
calc_factorial(3)=return 3*calc_factorial(2)=3*2*1
calc_factorial(2)=return 2*calc_factorial(1)= return 2*1 
'''
