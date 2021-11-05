# Raise Exception


def functionName( level ):
   if level < 1:
      raise ("Invalid level!", level)
      print("below raise .")
   else:
      print("level :",level)
   
      # The code below to this would not be executed
      # if we raise the exception

functionName(3)
