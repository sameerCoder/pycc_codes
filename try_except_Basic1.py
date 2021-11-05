# try except basic 1

try :
    a=int ( input (" Enter first number :"))
    b= int (input(" Enter second number :"))

    result = a/b
    print ("Result :",result)

    #print(c)

# except : this is generic exception .
#except(ZeroDivisionError) :
except:
     #except (ZeroDivisionError , TypeError) #Exception with many except.

  print ("Generic   Error .")

  

else :
    print("result is :",result)
    print (" successfully Division .")

    
finally:
    print("Error or not this will execute for sure .")

# After the Executing the try block , the control passes on to the else block .
# Hence the print statement in the else block is executed .


    
