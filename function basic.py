# Basic function .

def sumoftwo(a,b):
    ''' This function is useful to add two nubmer
        line2
        line3, which is known as functions documentation.'''
    sum1=0
    sum1=a+b
    print("sum of a+b:",sum1)
    return sum1


#returnvalue=sumoftwo(1,2)
#print(returnvalue)

#sumoftwo(11,12)
#sumoftwo()
c=sumoftwo(11,12)
print("print outside function ",c)

# Question
# WAP which have function doing subtraction of two number and return the value
# from function and print the return value outside the function.










def sub1(a,b):
    print("Subtraction value:",a-b)
    return (a-b)

returnvalue=sub1(20,10)
print("Subtraction value outside function:",returnvalue)


