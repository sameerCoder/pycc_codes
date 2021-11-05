# Function with more than one return value .

def  calc ( a , b ) :
  sum1 = a + b
  substract = a - b
  Multiply = a * b 
  return  sum1 ,substract ,Multiply 

a = int ( input ( " Enter  first number :"))
b = int ( input (  " Enter  second number :"))


print(calc(a,b))

s,sub,Mul=calc(a,b)                    
print ( " Sum :" , s )
print (  "Substract :",sub )
print ( "Multiply :" ,Mul )


