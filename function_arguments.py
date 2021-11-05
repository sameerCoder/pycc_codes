# Function  Arguments .
'''

#1. Required  Arguments .

def requiredvalue ( a ):
  print ( " number is :",a )

  return a

# Main ...

#a= int ( input ( " Enter a number :"))
a=10
#requiredvalue()

requiredvalue(a)



# 2. keyword Arguments .

def keywordargument ( roll_no , name ):
  print ( " Roll no : ",roll_no )
  print ( "Name is :", name)


roll=int ( input ( " Enter Roll No :"))
name = input( " Enter the name :"  )

keywordargument(name=name,roll_no=roll)



# 3.Default Arguments.

def defaultargument (roll_no , name , course="UG" ):

  print ( " Roll is :",roll_no)
  print ( " name is :",name)
  print ( "Course :",course)


roll=int(input ( " Enter the roll no :"))
name = input ( " Enter the name :")
course= input(" Enter the course :")

defaultargument(roll_no=roll,name=name)

#defaultargument(roll_no=roll,name=name,course=course)


# 4. Variable length Arguments

def variablearguments(*argument):

  print ("Result :")

  for i in argument :
    b=20
    print ( i+b )


variablearguments( 10)

variablearguments( 100 ,200 , 3000)

'''

# lambda function

x=lambda a:a*a


x(4)
print(list(x))























