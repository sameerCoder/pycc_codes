# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass
class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass
class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass
# our main program
# user guesses a number until he/she gets it right
# you need to guess this number
number = 10
for i in range(4):
#while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       elif i_num == number:
          print("you guessed it correct.")
          break
   except ValueTooSmallError:
	#print("This value is too small, try again!")
       	print("This value is too small, try again!")
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()
   finally:
       print("Thank you.")

print("Thank you.")

