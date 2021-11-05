# many exception


try :
    num1=int(input("Enter number1:"))
    num2=int(input("Enter number2:"))

    num1/num2
    print(num1/num2)


except ZeroDivisionError as argument2:
    print("num2 is given as zero.")

except ValueError as argument1:
    print("num1 or num2 has given different data type.")

except:
    print("Any Exceptional has occur.")

finally :
    a,b=10,12
    print(a+b)
    print("Thank you.")
    
    
