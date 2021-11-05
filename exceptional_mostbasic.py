#Excepiton handling.


#code line 1
#code line 2  10/0 # Error  # handle - message given .
# as normal next go to code line 3
#code line 3
#code line 4




'''

try:
    # Here we are writing Risky code  . 
    #print(10/2)
     #print(10/0)
    #c=10/0
    number=int(input("Enter number"))
    print(10/2)


except:
    # Here we are Handling code.
    print("Run time error occur , except block getting active.")
    print("There is an exceptional.")
    #print(4/2)
    #print(c)
    
else:
    print("No Error occur, so else block getting active ")
    #print(c)


'''
'''
try:
    num=int(input("Enter number"))
    print(4/2)
    print(10/0)

except ZeroDivisionError:
    print("Hi there is zero division error.")

except ValueError:
    print("Input the value correctly.")

except:
    print("Any Exception has occur.")

finally:
    print("Thank you.")
    
'''
try:
    num=int(input("Enter number"))
    print(10/0)

except ZeroDivisionError:
    print("Hi there is zero division error.")
    
except:
    print("Any Exception has occur.")
    


#except ValueError:
    #print("Input the value correctly.")

'''
try:
    num=int(input("Enter number"))
    print(10/0)

except ZeroDivisionError as msg:
    print("Hi there is zero division error.",msg)
    
except:
    print("Any Exception has occur.")


try :
    print(100/0)
    print("end of try.")

except ArithmeticError:
    print("This is Arithmetic Error.")
    #print(10/0)

except ZeroDivisionError:
    print("This is ZeroDivisionError.")
'''















