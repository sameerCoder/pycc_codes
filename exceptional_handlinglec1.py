# Exceptional Handling .

try :  
    a = 13
    #a=15
    if a > 6 : 
        # throws ZeroDivisionError for a = 3  
        b = a/(a-13) # 15/(15-3)=15/12 # 15/15-15 = 15/0
        #b=3/(3-3)
        #print()
      
    # throws NameError if a >= 6 
    print ("Value of b = ", b )
  
# note that braces () are necessary here for multiple exceptions

except(): 
    print ("\nError Occurred and Handled")
