# try except with Argument .


def display(a):

  try :

    return int (a)

  except ValueError as argument1:
  #except(ValueError):

    print("Argument does not contain number ",argument1)
    #print("Argument does not contain number ")


#print(display(10))

print(display("a"))
