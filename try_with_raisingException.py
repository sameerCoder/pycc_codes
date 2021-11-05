#try with raising an Exception .

a=int (input(" Enter a number :"))

try:

  if a<=0:
    raise ValueError ("Not a Positive Integer .")
  #raise is sending to except .

except ValueError as err:


    print("Error message:",err)
    
else:

    print("Positive Integer=",a)
