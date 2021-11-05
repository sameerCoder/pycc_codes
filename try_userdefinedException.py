# try with user defined exception.

class Error(Exception):
  # Base class for other exceptions.
  pass

class ValueTooSmall(Error):
  # raise when user input number is too small .
  pass 

class ValueTooLarge(Error):

  # raise when user input number is too large .
  pass

# Main Program

number = 10

while True:
  try:

    i_num=int(input(" Enter a number :"))

    if i_num <number:
      raise ValueTooSmall
    elif i_num > number :
      raise ValueTooLarge
    break

  except ValueTooSmall:
    print(" This value is too small then correct number  .")

  except ValueTooLarge:
    print(" This value is too large then correct number  .")
    
  except :
    print(" you entered wrong input data type .")
  finally:
    print(" Thank you.")
print(" Congratulation ! you guessed it correctly .")













    
  
