try :
	num1=int(input("Enter the number 1"))
	num2=int(input("Enter the number 2"))
	print("Result:",num1/num2)

# What all types of exception can occur by above code ?

# Exception1
#except ZeroDivisionError :
#	print("Can’t divide by zero. ")

#Exception2
except ValueError:
	print("Input only integer data type number. ")
except:
    print("general except.")
